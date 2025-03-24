from django.test import TestCase
from rest_framework.test import APIClient
from social_distribution.models import Author, FollowRequest
from social_distribution.serializers import AuthorSerializer
import uuid
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.models import User
import urllib.parse

class FollowingFriendsTests(TestCase):

    def setUp(self):
        # Create a dummy image for testing purposes.
        self.image = SimpleUploadedFile("test_image.jpg", b"fake_image_data", content_type="image/jpeg")
        self.client = APIClient()

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


    def test_send_follow_request(self):
        # Log in as Edwards
        self.client.login(username="edwards", password="password")
        # Define a variable bruce_uuid using the Bruce author"s id.
        bruce_uuid = self.bruce_author.id
        # Send follow request from Edwards to Bruce.
        response = self.client.post(f"/authors/{bruce_uuid}/follow/")
        self.assertEqual(response.status_code, 302)
        # Verify that a follow request exists.
        self.assertTrue(
            FollowRequest.objects.filter(sender=self.edwards_author, receiver__id=bruce_uuid, status="PENDING").exists()
        )

    def test_approve_follow_request(self):
        # Create a follow request from Edwards to Bruce.
        follow_req = FollowRequest.objects.create(sender=self.edwards_author, receiver=self.bruce_author)
        # Log in as Bruce (the receiver)
        self.client.login(username="bruce", password="password") 
        response = self.client.post(f"/follow_requests/{follow_req.id}/approve/") # type:ignore
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
        # Refresh the edwards_author instance and verify Bruce is no longer in Edwards" following.
        self.edwards_author.refresh_from_db()
        self.assertNotIn(self.bruce_author, self.edwards_author.following.all())



class FollowerAPITests(TestCase):
    def setUp(self):
        # Create users and corresponding authors for Edwards and Bruce
        self.client = APIClient()
        self.edwards_user = User.objects.create_user(username="edwards", password="password")
        self.bruce_user = User.objects.create_user(username="bruce", password="password")
        self.edwards_author = Author.objects.create(
            id=uuid.uuid4(),
            username="edwards",
            display_name="Edwards",
            github="https://github.com/edwards",
            profile_image=SimpleUploadedFile("test_image.jpg", b"fake_image_data", content_type="image/jpeg"),
            host="http://127.0.0.1:8000",
            user=self.edwards_user
        )
        self.bruce_author = Author.objects.create(
            id=uuid.uuid4(),
            username="bruce",
            display_name="Bruce Wayne",
            github="https://github.com/brucewayne",
            profile_image=SimpleUploadedFile("test_image.jpg", b"fake_image_data", content_type="image/jpeg"),
            host="http://127.0.0.1:8000",
            user=self.bruce_user
        )
    
    def test_get_followers_api(self):
        """
        Test GET on the followers API endpoint without a foreign author.
        """
        self.bruce_author.following.add(self.edwards_author)
        self.client.force_authenticate(user=self.edwards_user)  # type:ignore
        url = f"/api/authors/{self.edwards_author.id}/followers/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["type"], "followers") # type:ignore
        follower_ids = [follower["id"] for follower in response.data["followers"]] # type:ignore
        expected_id = AuthorSerializer(self.bruce_author).data["id"]
        self.assertIn(expected_id, follower_ids)
    
    def test_get_followers_api_specific(self):
        """
        Test GET on the followers API endpoint for a specific foreign author.
        """
        self.bruce_author.following.add(self.edwards_author)
        self.client.force_authenticate(user=self.edwards_user) # type:ignore
       
        foreign_id_encoded = urllib.parse.quote(str(self.bruce_author.fqid))
        url = f"/api/authors/{self.edwards_author.id}/followers/{foreign_id_encoded}/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["displayName"], self.bruce_author.display_name) # type:ignore
    
    def test_put_followers_api(self):
        """
        Test PUT on the followers API endpoint to add a follower.
        """
        
        self.client.force_authenticate(user=self.edwards_user) # type:ignore
       
        foreign_id_encoded = urllib.parse.quote(str(self.bruce_author.fqid))
        url = f"/api/authors/{self.edwards_author.id}/followers/{foreign_id_encoded}/"
        
        response = self.client.put(url)
        self.assertEqual(response.status_code, 200)
        
        self.assertIn(self.edwards_author, self.bruce_author.following.all())
    
    def test_delete_followers_api(self):
        """
        Test DELETE on the followers API endpoint to remove a follower.
        """
        
        self.bruce_author.following.add(self.edwards_author)
        self.client.force_authenticate(user=self.edwards_user) # type:ignore
        
        foreign_id_encoded = urllib.parse.quote(str(self.bruce_author.fqid))
        url = f"/api/authors/{self.edwards_author.id}/followers/{foreign_id_encoded}/"
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 200)
        
        self.assertNotIn(self.edwards_author, self.bruce_author.following.all())

class FollowRequestAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.edwards_user = User.objects.create_user(username="edwards", password="password")
        self.bruce_user = User.objects.create_user(username="bruce", password="password")
        self.edwards_author = Author.objects.create(
            id=uuid.uuid4(),
            username="edwards",
            display_name="Edwards",
            github="https://github.com/edwards",
            profile_image=SimpleUploadedFile("test_image.jpg", b"fake_image_data", content_type="image/jpeg"),
            host="http://127.0.0.1:8000",
            user=self.edwards_user
        )
        self.bruce_author = Author.objects.create(
            id=uuid.uuid4(),
            username="bruce",
            display_name="Bruce Wayne",
            github="https://github.com/brucewayne",
            profile_image=SimpleUploadedFile("test_image.jpg", b"fake_image_data", content_type="image/jpeg"),
            host="http://127.0.0.1:8000",
            user=self.bruce_user
        )
    
    def test_api_send_follow_request(self):
        """
        Test the API endpoint for sending a follow request.
        """
        self.client.force_authenticate(user=self.edwards_user) # type:ignore
        url = f"/api/authors/{self.bruce_author.id}/followrequest/"
        data = {"type": "follow"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["type"], "follow") # type:ignore
        self.assertIn("actor", response.data) # type:ignore
        self.assertIn("object", response.data) # type:ignore