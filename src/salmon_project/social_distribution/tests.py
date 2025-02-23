from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from .models import Author, Post, FollowRequest
import uuid
from django.core.files.uploadedfile import SimpleUploadedFile


# Create your tests here.
class AuthorTests(TestCase):

    def setUp(self):
        # Create a dummy image for testing purposes.
        self.image = SimpleUploadedFile("test_image.jpg", b"fake_image_data", content_type="image/jpeg")
        self.client = APIClient()

        # Existing author used for basic tests.
        self.author = Author.objects.create(
            id=uuid.uuid4(),
            username="testuser",
            display_name="Test User",
            github="https://github.com/testuser",
            profile_image=self.image,
            host="http://127.0.0.1:8000"
        )

        # --- New variables for follow/friend tests ---
        # Create two User objects for Edwards and Bruce.
        self.edwards_user = User.objects.create_user(username="edwards", password="password")
        self.bruce_user = User.objects.create_user(username="bruce", password="password")
        # Create corresponding Author objects.
        self.edwards_author = Author.objects.create(
            id=uuid.uuid4(),
            username="edwards",
            display_name="Edwards",
            github="https://github.com/edwards",
            profile_image=self.image,
            host="http://127.0.0.1:8000",
            user=self.edwards_user
        )
        self.bruce_author = Author.objects.create(
            id=uuid.uuid4(),
            username="bruce",
            display_name="Bruce Wayne",
            github="https://github.com/brucewayne",
            profile_image=self.image,
            host="http://127.0.0.1:8000",
            user=self.bruce_user
        )

    def test_get_authors(self):
        '''
        test for GET /api/authors/ to get all authors
        '''
        response = self.client.get("/api/authors/")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json(), "The response should not be empty")

    def test_get_author(self):
        '''
        test for GET /api/authors/{AUTHOR_ID}/ to get specific author
        '''
        response = self.client.get(f"/api/authors/{self.author.id}/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['username'], "testuser")

    def test_create_author(self):
        '''
        test for POST /api/authors/create/ to create an author
        '''
        data = {
            "username": "newuser",
            "display_name": "New User",
            "github": "https://github.com/newuser/",
            "host": "http://127.0.0.1:8000"
        }
        response = self.client.post("/api/authors/create/", data, format="json")
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()['username'], "newuser")

    def test_update_author(self):
        '''
        test for PUT /api/authors/{AUTHOR_ID}/update/ to update an author
        '''
        data = {
            "display_name": "Updated User",
            "github": "https://github.com/updateduser"
        }
        response = self.client.put(f"/api/authors/{self.author.id}/update/", data, format="json")
        self.assertEqual(response.status_code, 200)
        self.author.refresh_from_db()
        self.assertEqual(self.author.display_name, "Updated User")

    def test_invalid_author(self):
        '''
        test for GET /api/authors/{INVALID_ID} to return 404
        '''
        response = self.client.get("/api/authors/000000000000/")
        self.assertEqual(response.status_code, 404)

    def test_consistent_identity(self):
        '''
        testing user story: As an author, I want a consistent identity per node, so 
        that URLs to me/my posts are predictable and don't stop working.
        '''
        response = self.client.get(f"/api/authors/{self.author.id}/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["id"], f"http://127.0.0.1:8000/api/authors/{self.author.id}")

    def test_multiple_authors_on_node(self):
        '''
        testing user story: As a node admin, I want to host multiple authors on my node, 
        so I can have a friendly online community.
        '''
        another_author = Author.objects.create(
            id=uuid.uuid4(),
            username="anotheruser",
            display_name="Another User",
            github="https://github.com/anotheruser",
            host="http://127.0.0.1:8000"
        )
        response = self.client.get("/api/authors/")  # gets all authors
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.json()), 2)  # at least two authors exist

    def test_public_page(self):
        '''
        testing user story: As an author, I want a public page with my profile information, so that I can link people to it.
        '''
        response = self.client.get(reverse("profile", args=[self.author.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.author.display_name)

    def test_profile_page_public_posts(self):
        '''
        Testing user story: As an author, I want my profile page to show my public posts (most recent first), 
        so they can decide if they want to follow me.
        '''
        Post.objects.create(author=self.author, text="Test Post", visibility="PUBLIC")
        response = self.client.get(reverse("profile", args=[self.author.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Post")

    def test_manage_profile_web_browser(self):
        '''
        Testing user story: As an author, I want to be able to use my web browser to manage my profile, 
        so I don't have to use a clunky API.
        '''
        data = {
            "display_name": "Updated Again",
            "github": "https://github.com/updatedagain"
        }
        response = self.client.post(f"/authors/{self.author.id}/edit/", data)
        self.assertEqual(response.status_code, 302)
        self.author.refresh_from_db()
        self.assertEqual(self.author.display_name, "Updated Again")

    def test_send_follow_request(self):
        # Log in as Edwards
        self.client.login(username="edwards", password="password")
        # Define a variable bruce_uuid using the Bruce author's id.
        bruce_uuid = self.bruce_author.id
        # Send follow request from Edwards to Bruce.
        response = self.client.post(f"/authors/{bruce_uuid}/follow/")
        self.assertEqual(response.status_code, 302)
        # Verify that a follow request exists.
        self.assertTrue(
            FollowRequest.objects.filter(sender=self.edwards_author, receiver__id=bruce_uuid, status='PENDING').exists()
        )

    def test_approve_follow_request(self):
        # Create a follow request from Edwards to Bruce.
        follow_req = FollowRequest.objects.create(sender=self.edwards_author, receiver=self.bruce_author)
        # Log in as Bruce (the receiver)
        self.client.login(username="bruce", password="password")
        response = self.client.post(f"/follow_requests/{follow_req.id}/approve/")
        self.assertEqual(response.status_code, 302)
        follow_req.refresh_from_db()
        self.assertEqual(follow_req.status, "ACCEPTED")

    def test_unfollow_author(self):
        # Log in as Edwards and ensure he is following Bruce.
        self.client.login(username="edwards", password="password")
        self.edwards_author.following.add(self.bruce_author)
        # Unfollow Bruce.
        response = self.client.get(f"/authors/{self.bruce_author.id}/unfollow/")
        self.assertEqual(response.status_code, 302)
        # Refresh the edwards_author instance and verify Bruce is no longer in Edwards' following.
        self.edwards_author.refresh_from_db()
        self.assertNotIn(self.bruce_author, self.edwards_author.following.all())
