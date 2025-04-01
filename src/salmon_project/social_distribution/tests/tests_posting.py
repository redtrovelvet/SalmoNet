from django.urls import reverse
from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from social_distribution.models import Author, Post
import uuid
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.models import User
import base64

class PostingTests(APITestCase):
    def setUp(self):
        self.client = APIClient()

        # Create users
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.friend_user = User.objects.create_user(username="frienduser", password="friendpass")
        self.non_friend_user = User.objects.create_user(username="nonfrienduser", password="nonfriendpass")

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
            content="This is a public post.",
            visibility="PUBLIC"
        )

        self.friends_only_post = Post.objects.create(
            id=uuid.uuid4(),
            author=self.author,
            content="This is a friends-only post.",
            visibility="FRIENDS"
        )

        self.image_post = Post.objects.create(
            id=uuid.uuid4(),
            author=self.author,
            content=base64.b64encode(b"fake_image_data").decode("utf-8"),
            visibility="PUBLIC",
            content_type="image/jpeg;base64"
        )

    def test_get_public_post(self):
        """
        Test GET /api/authors/{AUTHOR_ID}/posts/{POST_ID}/ for a public post.
        Should return 200 for anyone.
        """
        url = reverse("posts_detail", args=[self.author.id, self.public_post.id])
        response = self.client.get(url)  # No authentication needed
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["content"], "This is a public post.")  # type:ignore

    def test_get_friends_only_post_as_friend(self):
        """
        Test GET /api/authors/{AUTHOR_ID}/posts/{POST_ID}/ for a friends-only post.
        Should return 200 if the requester is a friend.
        """
        self.client.force_authenticate(user=self.friend_user)  # Authenticate as friend # type:ignore
        url = reverse("posts_detail", args=[self.author.id, self.friends_only_post.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["content"], "This is a friends-only post.") # type:ignore

    def test_get_friends_only_post_as_non_friend(self):
        """
        Test GET /api/authors/{AUTHOR_ID}/posts/{POST_ID}/ for a friends-only post.
        Should return 403 if the requester is NOT a friend.
        """
        self.client.force_authenticate(user=self.non_friend_user)  # Authenticate as non-friend # type:ignore
        url = reverse("posts_detail", args=[self.author.id, self.friends_only_post.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.data["detail"], "You are not friends with the author.") # type:ignore

    def test_get_friends_only_post_unauthenticated(self):
        """
        Test GET /api/authors/{AUTHOR_ID}/posts/{POST_ID}/ for a friends-only post.
        Should return 403 if the requester is NOT authenticated.
        """
        url = reverse("posts_detail", args=[self.author.id, self.friends_only_post.id])
        response = self.client.get(url)  # No authentication
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.data["detail"], "Authentication required.") # type:ignore
        
    def test_create_post(self):
        """
        Test POST /api/authors/{AUTHOR_ID}/posts/ to create a new post.
        """
        self.client.force_authenticate(user=self.user) # type:ignore
        url = reverse("create_post", args=[self.author.id])
        data = {
            "content": "New Post",
            "visibility": "PUBLIC"
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertTrue(Post.objects.filter(content="New Post").exists())

    # NEW
    def test_create_post_unauthorized(self):
        """
        Test POST /api/authors/{AUTHOR_ID}/posts/ with unauthorized user.
        """
        url = reverse("create_post", args=[self.author.id])
        data = {
            "content": "New Post",
            "visibility": "PUBLIC"
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertFalse(Post.objects.filter(content="New Post").exists())
        
    def test_delete_post(self):
        """
        Test for DELETE /api/authors/{AUTHOR_ID}/posts/{POST_ID}/ to delete a post
        """ 
        self.client.force_authenticate(user=self.user) # type:ignore
        url = reverse("posts_detail", args=[self.author.id, self.public_post.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.public_post.refresh_from_db()
        self.assertEqual(self.public_post.visibility, "DELETED")

    def test_delete_post_unauthorized(self):
        """
        Test DELETE /api/authors/{AUTHOR_ID}/posts/{POST_ID}/ with unauthorized user.
        """
        self.client.force_authenticate(user=self.non_friend_user) # type:ignore
        url = reverse("posts_detail", args=[self.author.id, self.public_post.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_post(self):
        """
        Test PUT /api/authors/{AUTHOR_ID}/posts/{POST_ID}/ to update a post.
        """
        self.client.force_authenticate(user=self.user) # type:ignore
        url = reverse("posts_detail", args=[self.author.id, self.public_post.id])
        data = {"content": "Edited Post"}
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.public_post.refresh_from_db()
        self.assertEqual(self.public_post.content, "Edited Post")

    def test_update_post_unauthorized(self):
        """
        Test PUT /api/authors/{AUTHOR_ID}/posts/{POST_ID}/ with unauthorized user.
        """
        self.client.force_authenticate(user=self.non_friend_user) # type:ignore
        url = reverse("posts_detail", args=[self.author.id, self.public_post.id])
        data = {"content": "Edited Post"}
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # CHANGE
    def test_get_post_by_fqid(self):
        """
        Test GET /api/posts/{POST_FQID}/ to get a post by its fully qualified ID.
        """
        url = reverse("get_post_by_fqid", args=[self.public_post.fqid])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["content"], "This is a public post.") 
        
    def test_get_author_posts(self):
        """
        Test GET /api/authors/{AUTHOR_ID}/posts/ to get all posts by an author.
        """
        url = reverse("author_posts", args=[self.author.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["src"]), 2)  # Two public posts 

    def test_get_author_posts_authenticated(self):
        """
        Test GET /api/authors/{AUTHOR_ID}/posts/ with authenticated user.
        """
        self.client.force_authenticate(user=self.author.user) # type:ignore
        url = reverse("author_posts", args=[self.author.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["src"]), 3) # Two public posts and one friends-only post

    # NEW
    def test_get_author_posts_as_friend(self):
        """
        Test GET /api/authors/{AUTHOR_ID}/posts/ with authenticated friend.
        """
        self.client.force_authenticate(user=self.friend_user)
        url = reverse("author_posts", args=[self.author.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["src"]), 3) # Two public posts and one friends-only post
        
    def test_get_post_image(self):
        """
        Test GET /api/authors/{AUTHOR_ID}/posts/{POST_ID}/image/ to get an image post.
        """
        url = reverse("get_post_image", args=[self.author.id, self.image_post.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response["Content-Type"], "image/jpeg")

    def test_get_post_image_not_found(self):
        """
        Test GET /api/authors/{AUTHOR_ID}/posts/{POST_ID}/image/ for a non-image post.
        """
        url = reverse("get_post_image", args=[self.author.id, self.public_post.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    # NEW
    def test_get_post_by_fqid(self):
        """
        Test GET /api/posts/{POST_FQID}/image/ to get a post by its fully qualified ID.
        """
        url = reverse("get_postimage_by_fqid", args=[self.image_post.fqid])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response["Content-Type"], "image/jpeg")
    
    # NEW
    def test_get_post_by_fqid_not_found(self):
        """
        Test GET /api/posts/{POST_FQID}/image/ for a non-image post.
        """
        url = reverse("get_postimage_by_fqid", args=[self.public_post.fqid])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

