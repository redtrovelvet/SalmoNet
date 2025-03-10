from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from social_distribution.models import Author, Post, Comment, CommentLike, PostLike
import uuid

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
        self.assertEqual(response.json()["type"], "comments")
        self.assertEqual(response.json()["page"], f"http://127.0.0.1:8000/authors/{self.author.id}/posts/{self.post.id}")
        self.assertEqual(response.json()["id"], f"http://127.0.0.1:8000/api/authors/{self.author.id}/posts/{self.post.id}/comments")
        self.assertEqual(response.json()["page_number"], 1)
        self.assertEqual(response.json()["size"], 1)
        self.assertEqual(response.json()["count"], 1)
        self.assertEqual(len(response.json()["src"]), 1)
        
        # Validate each individual comment
        for comment in response.json()["src"]:
            self.validate_individual_comment(comment)

    # Method from Microsoft Copilot, "write a function to ensure an object of the correct format is returned", 2025-02-22
    def validate_individual_comment(self, comment):
        self.assertEqual(comment["type"], "comment")
        self.assertEqual(comment["author"]["type"], "author")
        self.assertEqual(comment["author"]["id"], f"http://127.0.0.1:8000/api/authors/{self.author.id}")
        self.assertEqual(comment["author"]["displayName"], "Test User")
        self.assertEqual(comment["comment"], "Test Comment")
        self.assertEqual(comment["contentType"], "text/plain")
        self.assertEqual(comment["id"], f"http://127.0.0.1:8000/api/authors/{self.author.id}/commented/{self.comment.id}")
        self.assertEqual(comment["post"], f"http://127.0.0.1:8000/api/authors/{self.author.id}/posts/{self.post.id}")
        self.assertEqual(comment["page"], f"http://127.0.0.1:8000/authors/{self.author.id}/posts/{self.post.id}")
        self.assertEqual(comment["likes"]["type"], "likes")
        self.assertEqual(comment["likes"]["id"], f"http://127.0.0.1:8000/api/authors/{self.author.id}/commented/{self.comment.id}/likes")
        self.assertEqual(comment["likes"]["page"], f"http://127.0.0.1:8000/authors/{self.author.id}/comments/{self.comment.id}")
        self.assertEqual(comment["likes"]["page_number"], 1)
        self.assertEqual(comment["likes"]["size"], 0)
        self.assertEqual(comment["likes"]["count"], 0)
        self.assertEqual(len(comment["likes"]["src"]), 0)

    def test_get_author_comments(self):
        """
        test for GET /api/authors/{AUTHOR_ID}/posts/{POST_ID}/comments/ to get all comments on a post
        """
        url = reverse("get_author_comments", args=[self.author.id, self.post.id])
        response = self.client.get(url)
        self.validate_comments_object(response)

    def test_get_comments(self):
        """
        test for GET /api/posts/{POST_ID}/comments/ to get all comments on a post
        """
        url = reverse("get_comments", args=[self.post.id])
        response = self.client.get(url)
        self.validate_comments_object(response)

    def test_get_remote_comment(self):
        """
        test for GET /api/authors/{AUTHOR_ID}/post/{POST_ID}/comments/{COMMENT_ID}/ to get a specific comment
        """
        url = reverse("get_remote_comment", args=[self.author.id, self.post.id, self.comment.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json(), "The response should not be empty")
        self.validate_individual_comment(response.json())

    def test_commented(self):
        """
        test for GET /api/authors/{AUTHOR_ID}/commented/ to get all comments by an author
        and for POST /api/authors/{AUTHOR_ID}/commented/ to create a new comment
        """
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
        """
        test for GET /api/authors/{AUTHOR_ID}/commented/{COMMENT_ID}/ to get a specific comment by an author
        """
        url = reverse("get_author_comment", args=[self.author.id, self.comment.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.validate_individual_comment(response.json())

    def test_get_comment(self):
        """
        test for GET /api/commented/{COMMENT_ID}/ to get a specific comment
        """
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
        self.assertEqual(response.json()["type"], "likes")
        if like_type == "post":
            self.assertEqual(response.json()["page"], f"http://127.0.0.1:8000/authors/{self.author.id}/posts/{self.post.id}")
            self.assertEqual(response.json()["id"], f"http://127.0.0.1:8000/api/authors/{self.author.id}/posts/{self.post.id}/likes")
        elif like_type == "comment":
            self.assertEqual(response.json()["page"], f"http://127.0.0.1:8000/authors/{self.author.id}/comments/{self.comment.id}")
            self.assertEqual(response.json()["id"], f"http://127.0.0.1:8000/api/authors/{self.author.id}/commented/{self.comment.id}/likes")
                             
        self.assertEqual(response.json()["page_number"], 1)
        self.assertEqual(response.json()["size"], 1)
        self.assertEqual(response.json()["count"], 1)
        self.assertEqual(len(response.json()["src"]), 1)
        
        # Validate each individual like
        if like_type == "post":
            for like in response.json()["src"]:
                self.validate_individual_post_like(like)
        elif like_type == "comment":
            for like in response.json()["src"]:
                self.validate_individual_comment_like(like)

    # Method from Microsoft Copilot, "write similar functions to ensure likes match this format", 2025-02-22
    def validate_individual_post_like(self, like):
        self.assertEqual(like["type"], "like")
        self.assertEqual(like["author"]["type"], "author")
        self.assertEqual(like["author"]["id"], f"http://127.0.0.1:8000/api/authors/{self.author.id}")
        self.assertEqual(like["author"]["displayName"], "Test User")
        self.assertEqual(like["author"]["github"], "https://github.com/testuser")
        self.assertEqual(like["id"], f"http://127.0.0.1:8000/api/authors/{self.author.id}/liked/{self.post_like.id}")
        self.assertEqual(like["object"], f"http://127.0.0.1:8000/api/authors/{self.author.id}/posts/{self.post.id}")

    # Method from Microsoft Copilot, "write similar functions to ensure likes match this format", 2025-02-22
    def validate_individual_comment_like(self, like):
        self.assertEqual(like["type"], "like")
        self.assertEqual(like["author"]["type"], "author")
        self.assertEqual(like["author"]["id"], f"http://127.0.0.1:8000/api/authors/{self.author.id}")
        self.assertEqual(like["author"]["displayName"], "Test User")
        self.assertEqual(like["author"]["github"], "https://github.com/testuser")
        self.assertEqual(like["id"], f"http://127.0.0.1:8000/api/authors/{self.author.id}/liked/{self.comment_like.id}")
        self.assertEqual(like["object"], f"http://127.0.0.1:8000/api/authors/{self.author.id}/commented/{self.comment.id}")
        
    
    def test_get_post_likes(self):
        """
        test for GET /api/authors/{AUTHOR_ID}/posts/{POST_ID}/likes/ to get all likes on a post
        """
        url = reverse("get_post_likes", args=[self.author.id, self.post.id])
        response = self.client.get(url)
        self.validate_likes_object(response, "post")

    def test_get_likes(self):
        """
        test for GET /api/posts/{POST_ID}/likes/ to get all likes on a post
        """
        url = reverse("get_likes", args=[self.post.id])
        response = self.client.get(url)
        self.validate_likes_object(response, "post")

    def test_get_comment_likes(self):
        """
        test for GET /api/authors/{AUTHOR_ID}/posts/{POST_ID}/comments/{COMMENT_ID}/likes/ to get all likes on a comment
        """
        url = reverse("get_comment_likes", args=[self.author.id, self.post.id, self.comment.id])
        response = self.client.get(url)
        self.validate_likes_object(response, "comment")

    def test_get_author_liked(self):
        """
        test for GET /api/authors/{AUTHOR_ID}/liked/ to get all likes by an author
        """
        url = reverse("get_author_liked", args=[self.author.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json(), "The response should not be empty")
        self.assertEqual(response.json()["type"], "likes")
        self.assertEqual(response.json()["page"], f"http://127.0.0.1:8000/authors/{self.author.id}/likes")
        self.assertEqual(response.json()["id"], f"http://127.0.0.1:8000/api/authors/{self.author.id}/likes")
        self.assertEqual(response.json()["page_number"], 1)
        self.assertEqual(response.json()["size"], 2)
        self.assertEqual(response.json()["count"], 2)
        self.assertEqual(len(response.json()["src"]), 2)

        # Validate each individual like
        for like in response.json()["src"]:
            if like["object"] == f"http://127.0.0.1:8000/api/authors/{self.author.id}/posts/{self.post.id}":
                self.validate_individual_post_like(like)
            elif like["object"] == f"http://127.0.0.1:8000/api/authors/{self.author.id}/commented/{self.comment.id}":
                self.validate_individual_comment_like(like)        

    def test_get_author_like(self):
        """
        test for GET /api/authors/{AUTHOR_ID}/liked/{LIKE_ID} to get a specific like by an author
        """
        url = reverse("get_author_like", args=[self.author.id, self.post_like.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.validate_individual_post_like(response.json())

        url = reverse("get_author_like", args=[self.author.id, self.comment_like.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.validate_individual_comment_like(response.json())

    def test_get_like(self):
        """
        test for GET /api/liked/{LIKE_ID}/ to get a specific like
        """
        url = reverse("get_like", args=[self.post_like.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.validate_individual_post_like(response.json())

    def test_like_post(self):
        """
        test for POST /api/authors/{AUTHOR_ID}/posts/{POST_ID}/liked/ to like a post
        """
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
        """
        test for POST /api/authors/{AUTHOR_ID}/comments/{COMMENT_ID}/liked/ to like a comment
        """
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
