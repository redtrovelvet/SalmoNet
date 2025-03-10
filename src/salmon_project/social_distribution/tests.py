from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from .models import Author, Post, Comment, CommentLike, PostLike, FollowRequest
from .serializers import AuthorSerializer, PostSerializer
import uuid
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.models import User
import urllib.parse

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

class CommentTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.author = Author.objects.create(
            id=uuid.uuid4(),
            username = "testuser",
            display_name = "Test User",
            github = "https://github.com/testuser",
            profile_image = None,
            host="http://127.0.0.1:8000"
        )

        self.post = Post.objects.create(
            id=uuid.uuid4(),
            author=self.author,
            text="Test Post",
            visibility="PUBLIC"
        )

        self.comment = Comment.objects.create(
            id=uuid.uuid4(),
            post=self.post,
            author=self.author,
            comment="Test Comment",
            content_type="text/plain"
        )

    # Method from Microsoft Copilot, "write a function to ensure an object of the correct format is returned", 2025-02-22
    def validate_comments_object(self, response):
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json(), "The response should not be empty")
        self.assertEqual(response.json()['type'], "comments")
        self.assertEqual(response.json()['page'], f"http://127.0.0.1:8000/authors/{self.author.id}/posts/{self.post.id}")
        self.assertEqual(response.json()['id'], f"http://127.0.0.1:8000/api/authors/{self.author.id}/posts/{self.post.id}/comments")
        self.assertEqual(response.json()['page_number'], 1)
        self.assertEqual(response.json()['size'], 1)
        self.assertEqual(response.json()['count'], 1)
        self.assertEqual(len(response.json()['src']), 1)
        
        # Validate each individual comment
        for comment in response.json()['src']:
            self.validate_individual_comment(comment)

    # Method from Microsoft Copilot, "write a function to ensure an object of the correct format is returned", 2025-02-22
    def validate_individual_comment(self, comment):
        self.assertEqual(comment['type'], "comment")
        self.assertEqual(comment['author']['type'], "author")
        self.assertEqual(comment['author']['id'], f"http://127.0.0.1:8000/api/authors/{self.author.id}")
        self.assertEqual(comment['author']['displayName'], "Test User")
        self.assertEqual(comment['comment'], "Test Comment")
        self.assertEqual(comment['contentType'], "text/plain")
        self.assertEqual(comment['id'], f"http://127.0.0.1:8000/api/authors/{self.author.id}/commented/{self.comment.id}")
        self.assertEqual(comment['post'], f"http://127.0.0.1:8000/api/authors/{self.author.id}/posts/{self.post.id}")
        self.assertEqual(comment['page'], f"http://127.0.0.1:8000/authors/{self.author.id}/posts/{self.post.id}")
        self.assertEqual(comment['likes']['type'], "likes")
        self.assertEqual(comment['likes']['id'], f"http://127.0.0.1:8000/api/authors/{self.author.id}/commented/{self.comment.id}/likes")
        self.assertEqual(comment['likes']['page'], f"http://127.0.0.1:8000/authors/{self.author.id}/comments/{self.comment.id}")
        self.assertEqual(comment['likes']['page_number'], 1)
        self.assertEqual(comment['likes']['size'], 0)
        self.assertEqual(comment['likes']['count'], 0)
        self.assertEqual(len(comment['likes']['src']), 0)

    def test_get_author_comments(self):
        '''
        test for GET /api/authors/{AUTHOR_ID}/posts/{POST_ID}/comments/ to get all comments on a post
        '''
        url = reverse("get_author_comments", args=[self.author.id, self.post.id])
        response = self.client.get(url)
        self.validate_comments_object(response)

    def test_get_comments(self):
        '''
        test for GET /api/posts/{POST_ID}/comments/ to get all comments on a post
        '''
        url = reverse("get_comments", args=[self.post.id])
        response = self.client.get(url)
        self.validate_comments_object(response)

    def test_get_remote_comment(self):
        '''
        test for GET /api/authors/{AUTHOR_ID}/post/{POST_ID}/comments/{COMMENT_ID}/ to get a specific comment
        '''
        url = reverse("get_remote_comment", args=[self.author.id, self.post.id, self.comment.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json(), "The response should not be empty")
        self.validate_individual_comment(response.json())

    def test_commented(self):
        '''
        test for GET /api/authors/{AUTHOR_ID}/commented/ to get all comments by an author
        and for POST /api/authors/{AUTHOR_ID}/commented/ to create a new comment
        '''
        # GET request
        url = reverse("commented", args=[self.author.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        for comment in response.json():
            self.validate_individual_comment(comment)
        
        # POST request to create a new comment on the post
        # TODO: make it consistent with the comment json standard
        data = {
            "type": "comment",
            "comment": "New Comment",
            "post": self.post.id,
            "contentType": "text/plain",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Comment.objects.count(), 2)
        comment = Comment.objects.get(comment="New Comment")
        self.assertEqual(comment.author, self.author)

    def test_get_author_comment(self):
        '''
        test for GET /api/authors/{AUTHOR_ID}/commented/{COMMENT_ID}/ to get a specific comment by an author
        '''
        url = reverse("get_author_comment", args=[self.author.id, self.comment.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.validate_individual_comment(response.json())

    def test_get_comment(self):
        '''
        test for GET /api/commented/{COMMENT_ID}/ to get a specific comment
        '''
        url = reverse("get_comment", args=[self.comment.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.validate_individual_comment(response.json())

class LikeTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.author = Author.objects.create(
            id=uuid.uuid4(),
            username = "testuser",
            display_name = "Test User",
            github = "https://github.com/testuser",
            profile_image = None,
            host="http://127.0.0.1:8000"
        )

        self.post = Post.objects.create(
            id=uuid.uuid4(),
            author=self.author,
            text="Test Post",
            visibility="PUBLIC"
        )

        self.comment = Comment.objects.create(
            id=uuid.uuid4(),
            post=self.post,
            author=self.author,
            comment="Test Comment",
            content_type="text/plain"
        )

        self.post_like = PostLike.objects.create(
            id=uuid.uuid4(),
            object=self.post,
            author=self.author
        )

        self.comment_like = CommentLike.objects.create(
            id=uuid.uuid4(),
            object=self.comment,
            author=self.author
        )

    # Method from Microsoft Copilot, "write similar functions to ensure likes match this format", 2025-02-22
    def validate_likes_object(self, response, like_type="post"):
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json(), "The response should not be empty")
        self.assertEqual(response.json()['type'], "likes")
        if like_type == "post":
            self.assertEqual(response.json()['page'], f"http://127.0.0.1:8000/authors/{self.author.id}/posts/{self.post.id}")
            self.assertEqual(response.json()['id'], f"http://127.0.0.1:8000/api/authors/{self.author.id}/posts/{self.post.id}/likes")
        elif like_type == "comment":
            self.assertEqual(response.json()['page'], f"http://127.0.0.1:8000/authors/{self.author.id}/comments/{self.comment.id}")
            self.assertEqual(response.json()['id'], f"http://127.0.0.1:8000/api/authors/{self.author.id}/commented/{self.comment.id}/likes")
                             
        self.assertEqual(response.json()['page_number'], 1)
        self.assertEqual(response.json()['size'], 1)
        self.assertEqual(response.json()['count'], 1)
        self.assertEqual(len(response.json()['src']), 1)
        
        # Validate each individual like
        if like_type == "post":
            for like in response.json()['src']:
                self.validate_individual_post_like(like)
        elif like_type == "comment":
            for like in response.json()['src']:
                self.validate_individual_comment_like(like)

    # Method from Microsoft Copilot, "write similar functions to ensure likes match this format", 2025-02-22
    def validate_individual_post_like(self, like):
        self.assertEqual(like['type'], "like")
        self.assertEqual(like['author']['type'], "author")
        self.assertEqual(like['author']['id'], f"http://127.0.0.1:8000/api/authors/{self.author.id}")
        self.assertEqual(like['author']['displayName'], "Test User")
        self.assertEqual(like['author']['github'], "https://github.com/testuser")
        self.assertEqual(like['id'], f"http://127.0.0.1:8000/api/authors/{self.author.id}/liked/{self.post_like.id}")
        self.assertEqual(like['object'], f"http://127.0.0.1:8000/api/authors/{self.author.id}/posts/{self.post.id}")

    # Method from Microsoft Copilot, "write similar functions to ensure likes match this format", 2025-02-22
    def validate_individual_comment_like(self, like):
        self.assertEqual(like['type'], "like")
        self.assertEqual(like['author']['type'], "author")
        self.assertEqual(like['author']['id'], f"http://127.0.0.1:8000/api/authors/{self.author.id}")
        self.assertEqual(like['author']['displayName'], "Test User")
        self.assertEqual(like['author']['github'], "https://github.com/testuser")
        self.assertEqual(like['id'], f"http://127.0.0.1:8000/api/authors/{self.author.id}/liked/{self.comment_like.id}")
        self.assertEqual(like['object'], f"http://127.0.0.1:8000/api/authors/{self.author.id}/commented/{self.comment.id}")
        
    
    def test_get_post_likes(self):
        '''
        test for GET /api/authors/{AUTHOR_ID}/posts/{POST_ID}/likes/ to get all likes on a post
        '''
        url = reverse("get_post_likes", args=[self.author.id, self.post.id])
        response = self.client.get(url)
        self.validate_likes_object(response, "post")

    def test_get_likes(self):
        '''
        test for GET /api/posts/{POST_ID}/likes/ to get all likes on a post
        '''
        url = reverse("get_likes", args=[self.post.id])
        response = self.client.get(url)
        self.validate_likes_object(response, "post")

    def test_get_comment_likes(self):
        '''
        test for GET /api/authors/{AUTHOR_ID}/posts/{POST_ID}/comments/{COMMENT_ID}/likes/ to get all likes on a comment
        '''
        url = reverse("get_comment_likes", args=[self.author.id, self.post.id, self.comment.id])
        response = self.client.get(url)
        self.validate_likes_object(response, "comment")

    def test_get_author_liked(self):
        '''
        test for GET /api/authors/{AUTHOR_ID}/liked/ to get all likes by an author
        '''
        url = reverse("get_author_liked", args=[self.author.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json(), "The response should not be empty")
        self.assertEqual(response.json()['type'], "likes")
        self.assertEqual(response.json()['page'], f"http://127.0.0.1:8000/authors/{self.author.id}/likes")
        self.assertEqual(response.json()['id'], f"http://127.0.0.1:8000/api/authors/{self.author.id}/likes")
        self.assertEqual(response.json()['page_number'], 1)
        self.assertEqual(response.json()['size'], 2)
        self.assertEqual(response.json()['count'], 2)
        self.assertEqual(len(response.json()['src']), 2)

        # Validate each individual like
        for like in response.json()['src']:
            if like['object'] == f"http://127.0.0.1:8000/api/authors/{self.author.id}/posts/{self.post.id}":
                self.validate_individual_post_like(like)
            elif like['object'] == f"http://127.0.0.1:8000/api/authors/{self.author.id}/commented/{self.comment.id}":
                self.validate_individual_comment_like(like)        

    def test_get_author_like(self):
        '''
        test for GET /api/authors/{AUTHOR_ID}/liked/{LIKE_ID} to get a specific like by an author
        '''
        url = reverse("get_author_like", args=[self.author.id, self.post_like.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.validate_individual_post_like(response.json())

        url = reverse("get_author_like", args=[self.author.id, self.comment_like.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.validate_individual_comment_like(response.json())

    def test_get_like(self):
        '''
        test for GET /api/liked/{LIKE_ID}/ to get a specific like
        '''
        url = reverse("get_like", args=[self.post_like.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.validate_individual_post_like(response.json())

    def test_like_post(self):
        '''
        test for POST /api/authors/{AUTHOR_ID}/posts/{POST_ID}/liked/ to like a post
        '''
        # Clear likes before testing
        PostLike.objects.all().delete()

        self.assertEqual(PostLike.objects.count(), 0)
        url = reverse("like_post", args=[self.author.id, self.post.id])
        body = {
            "type": "like",
        }
        response = self.client.post(url, body, format="json")
        self.assertEqual(response.status_code, 201)
        self.assertEqual(PostLike.objects.count(), 1)
        like = PostLike.objects.get(author=self.author)
        self.assertEqual(like.object, self.post)

        # Test for liking the same post again
        response = self.client.post(url, body, format="json")
        self.assertEqual(response.status_code, 201)
        self.assertEqual(PostLike.objects.count(), 0)

    def test_like_comment(self):
        '''
        test for POST /api/authors/{AUTHOR_ID}/comments/{COMMENT_ID}/liked/ to like a comment
        '''
        # Clear likes before testing
        CommentLike.objects.all().delete()

        self.assertEqual(CommentLike.objects.count(), 0)
        url = reverse("like_comment", args=[self.author.id, self.comment.id])
        body = {
            "type": "like",
        }
        response = self.client.post(url, body, format="json")
        self.assertEqual(response.status_code, 201)
        self.assertEqual(CommentLike.objects.count(), 1)
        like = CommentLike.objects.get(author=self.author)
        self.assertEqual(like.object, self.comment)

        # Test for liking the same comment again
        response = self.client.post(url, body, format="json")
        self.assertEqual(response.status_code, 201)
        self.assertEqual(CommentLike.objects.count(), 0)
        
class PostTests(APITestCase):
    def setUp(self):
        self.client = APIClient()

        # Create users
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.friend_user = User.objects.create_user(username='frienduser', password='friendpass')
        self.non_friend_user = User.objects.create_user(username='nonfrienduser', password='nonfriendpass')

        # Create authors
        self.author = Author.objects.create(
            id=uuid.uuid4(),
            username="testuser",
            display_name="Test User",
            github="https://github.com/testuser",
            profile_image=None,
            host="http://127.0.0.1:8000"
        )

        self.friend_author = Author.objects.create(
            id=uuid.uuid4(),
            username="frienduser",
            display_name="Friend User",
            github="https://github.com/frienduser",
            profile_image=None,
            host="http://127.0.0.1:8000"
        )

        self.non_friend_author = Author.objects.create(
            id=uuid.uuid4(),
            username="nonfrienduser",
            display_name="Non-Friend User",
            github="https://github.com/nonfrienduser",
            profile_image=None,
            host="http://127.0.0.1:8000"
        )

        # Link users to authors AFTER creation
        self.author.user = self.user
        self.author.save()

        self.friend_author.user = self.friend_user
        self.friend_author.save()

        self.non_friend_author.user = self.non_friend_user
        self.non_friend_author.save()

        # Establish friendship (two-way follow)
        self.author.following.add(self.friend_author)
        self.friend_author.following.add(self.author)

        # Create posts
        self.public_post = Post.objects.create(
            id=uuid.uuid4(),
            author=self.author,
            text="This is a public post.",
            visibility="PUBLIC"
        )

        self.friends_only_post = Post.objects.create(
            id=uuid.uuid4(),
            author=self.author,
            text="This is a friends-only post.",
            visibility="FRIENDS"
        )

        self.image_post = Post.objects.create(
            id=uuid.uuid4(),
            author=self.author,
            text="Test Image Post",
            visibility="PUBLIC",
            content_type="image/jpeg",
            image=SimpleUploadedFile("test_image.jpg", b"fake_image_data", content_type="image/jpeg")
        )

    def test_get_public_post(self):
        """
        Test GET /api/authors/{AUTHOR_ID}/posts/{POST_ID}/ for a public post.
        Should return 200 for anyone.
        """
        url = reverse("get_post", args=[self.author.id, self.public_post.id])
        response = self.client.get(url)  # No authentication needed
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["text"], "This is a public post.")

    def test_get_friends_only_post_as_friend(self):
        """
        Test GET /api/authors/{AUTHOR_ID}/posts/{POST_ID}/ for a friends-only post.
        Should return 200 if the requester is a friend.
        """
        self.client.force_authenticate(user=self.friend_user)  # Authenticate as friend
        url = reverse("get_post", args=[self.author.id, self.friends_only_post.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["text"], "This is a friends-only post.")

    def test_get_friends_only_post_as_non_friend(self):
        """
        Test GET /api/authors/{AUTHOR_ID}/posts/{POST_ID}/ for a friends-only post.
        Should return 403 if the requester is NOT a friend.
        """
        self.client.force_authenticate(user=self.non_friend_user)  # Authenticate as non-friend
        url = reverse("get_post", args=[self.author.id, self.friends_only_post.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.data["detail"], "You are not friends with the author.")

    def test_get_friends_only_post_unauthenticated(self):
        """
        Test GET /api/authors/{AUTHOR_ID}/posts/{POST_ID}/ for a friends-only post.
        Should return 403 if the requester is NOT authenticated.
        """
        url = reverse("get_post", args=[self.author.id, self.friends_only_post.id])
        response = self.client.get(url)  # No authentication
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.data["detail"], "Authentication required.")
        
    def test_create_post(self):
        """
        Test POST /api/authors/{AUTHOR_ID}/posts/ to create a new post.
        """
        self.client.force_authenticate(user=self.user)
        url = reverse("create_post", args=[self.author.id])
        data = {
            "text": "New Post",
            "visibility": "PUBLIC"
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertTrue(Post.objects.filter(text="New Post").exists())
        
    def test_delete_post(self):
        """
        Test for DELETE /api/authors/{AUTHOR_ID}/posts/{POST_ID}/ to delete a post
        """
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(f"/api/authors/{self.author.id}/posts/{self.public_post.id}/delete/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.public_post.refresh_from_db()
        self.assertEqual(self.public_post.visibility, "DELETED")

    def test_delete_post_unauthorized(self):
        """
        Test DELETE /api/authors/{AUTHOR_ID}/posts/{POST_ID}/ with unauthorized user.
        """
        self.client.force_authenticate(user=self.non_friend_user)
        url = reverse("delete_post", args=[self.author.id, self.public_post.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_post(self):
        """
        Test PUT /api/authors/{AUTHOR_ID}/posts/{POST_ID}/ to update a post.
        """
        self.client.force_authenticate(user=self.user)
        url = reverse("update_post", args=[self.author.id, self.public_post.id])
        data = {"text": "Edited Post"}
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.public_post.refresh_from_db()
        self.assertEqual(self.public_post.text, "Edited Post")

    def test_update_post_unauthorized(self):
        """
        Test PUT /api/authors/{AUTHOR_ID}/posts/{POST_ID}/ with unauthorized user.
        """
        self.client.force_authenticate(user=self.non_friend_user)
        url = reverse("update_post", args=[self.author.id, self.public_post.id])
        data = {"text": "Edited Post"}
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_post_by_fqid(self):
        """
        Test GET /api/posts/{POST_FQID}/ to get a post by its fully qualified ID.
        """
        url = reverse("get_post_by_fqid", args=[self.public_post.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["text"], "This is a public post.")
        
    def test_get_author_posts(self):
        """
        Test GET /api/authors/{AUTHOR_ID}/posts/ to get all posts by an author.
        """
        url = reverse("get_author_posts", args=[self.author.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Two public posts

    def test_get_author_posts_authenticated(self):
        """
        Test GET /api/authors/{AUTHOR_ID}/posts/ with authenticated user.
        """
        self.client.force_authenticate(user=self.author.user)
        url = reverse("get_author_posts", args=[self.author.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3) # Two public posts and one friends-only post
        
    def test_get_post_image(self):
        """
        Test GET /api/authors/{AUTHOR_ID}/posts/{POST_ID}/image/ to get an image post.
        """
        url = reverse("get_post_image", args=[self.author.id, self.image_post.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response['Content-Type'], "image/jpeg")

    def test_get_post_image_not_found(self):
        """
        Test GET /api/authors/{AUTHOR_ID}/posts/{POST_ID}/image/ for a non-image post.
        """
        url = reverse("get_post_image", args=[self.author.id, self.public_post.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


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
        self.client.force_authenticate(user=self.edwards_user)
        url = f"/api/authors/{self.edwards_author.id}/followers/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["type"], "followers")
        follower_ids = [follower["id"] for follower in response.data["followers"]]
        expected_id = AuthorSerializer(self.bruce_author).data["id"]
        self.assertIn(expected_id, follower_ids)
    
    def test_get_followers_api_specific(self):
        """
        Test GET on the followers API endpoint for a specific foreign author.
        """
        self.bruce_author.following.add(self.edwards_author)
        self.client.force_authenticate(user=self.edwards_user)
       
        foreign_id_encoded = urllib.parse.quote(str(self.bruce_author.id))
        url = f"/api/authors/{self.edwards_author.id}/followers/{foreign_id_encoded}/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["username"], self.bruce_author.username)
    
    def test_put_followers_api(self):
        """
        Test PUT on the followers API endpoint to add a follower.
        """
        
        self.client.force_authenticate(user=self.edwards_user)
       
        foreign_id_encoded = urllib.parse.quote(str(self.bruce_author.id))
        url = f"/api/authors/{self.edwards_author.id}/followers/{foreign_id_encoded}/"
        
        response = self.client.put(url)
        self.assertEqual(response.status_code, 200)
        
        self.assertIn(self.edwards_author, self.bruce_author.following.all())
    
    def test_delete_followers_api(self):
        """
        Test DELETE on the followers API endpoint to remove a follower.
        """
        
        self.bruce_author.following.add(self.edwards_author)
        self.client.force_authenticate(user=self.edwards_user)
        
        foreign_id_encoded = urllib.parse.quote(str(self.bruce_author.id))
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
        self.client.force_authenticate(user=self.edwards_user)
        url = f"/api/authors/{self.bruce_author.id}/followrequest/"
        data = {"type": "follow"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["type"], "follow")
        self.assertIn("actor", response.data)
        self.assertIn("object", response.data)
