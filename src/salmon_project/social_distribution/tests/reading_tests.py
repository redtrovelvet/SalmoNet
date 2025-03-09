from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from social_distribution.models import Author, Post
import uuid
from django.contrib.auth.models import User
import time

class ReadingTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        
        self.user = User.objects.create_user(username="user", password="userpass")
        self.friend_user = User.objects.create_user(username="friend", password="friendpass")
        self.other_user = User.objects.create_user(username="other", password="otherpass")
        
        self.user_author = Author.objects.create(
            id=uuid.uuid4(),
            username="user",
            display_name="User Author",
            github="https://github.com/user",
            host="http://127.0.0.1:8000",
            user=self.user
        )
        self.friend_author = Author.objects.create(
            id=uuid.uuid4(),
            username="friend",
            display_name="Friend Author",
            github="https://github.com/friend",
            host="http://127.0.0.1:8000",
            user=self.friend_user
        )
        self.other_author = Author.objects.create(
            id=uuid.uuid4(),
            username="other",
            display_name="Other Author",
            github="https://github.com/other",
            host="http://127.0.0.1:8000",
            user=self.other_user
        )
        
        self.user_author.following.add(self.friend_author)
        self.friend_author.following.add(self.user_author)
        
        self.public_post = Post.objects.create(
            id=uuid.uuid4(),
            author=self.other_author,
            text="Public Post by Other",
            visibility="PUBLIC",
            content_type="text/plain"
        )
        self.friends_only_post = Post.objects.create(
            id=uuid.uuid4(),
            author=self.friend_author,
            text="Friends-only Post by Friend",
            visibility="FRIENDS",
            content_type="text/plain"
        )
        self.unlisted_post = Post.objects.create(
            id=uuid.uuid4(),
            author=self.friend_author,
            text="Unlisted Post by Friend",
            visibility="UNLISTED",
            content_type="text/plain"
        )

        self.deleted_post = Post.objects.create(
            id=uuid.uuid4(),
            author=self.friend_author,
            text="Deleted Post",
            visibility="DELETED",
            content_type="text/plain"
        )
    
    def test_show_public_posts(self):
        """
        The public stream should show only public posts if you are an unauthenticated user
        Testing user story: As an author, I want my stream page to show me all the
        public posts my node knows about, so I can find new people to follow.
        """
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Public Post by Other")
        self.assertNotContains(response, "Friends-only Post by Friend")
        self.assertNotContains(response, "Unlisted Post by Friend")
        self.assertNotContains(response, "Deleted Post")
    
    def test_show_friends_and_unlisted_posts(self):
        """
        Testing user story: As an author, I want my stream page to show me all the 
        unlisted and friends-only posts of all the authors I follow.
        """
        self.client.login(username="user", password="userpass")
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Friends-only Post by Friend")
        self.assertContains(response, "Unlisted Post by Friend")
        self.assertNotContains(response, "Deleted Post")

    def test_order_of_stream_if_edit_post(self):
        """
        Testing user story: As an author, I want my stream page to show me the most recent 
        version of a post if it has been edited.
        """
        response_initial = self.client.get(reverse("index"))
        self.assertContains(response_initial, "Public Post by Other")
        self.public_post.text = "Public Post Updated"
        self.public_post.save()
        response_updated = self.client.get(reverse("index"))
        self.assertContains(response_updated, "Public Post Updated")
        self.assertNotContains(response_updated, "Public Post by Other")

    def test_do_not_show_deleted_posts(self):
        """
        Testing user story: As an author, I want my stream page to not show me posts that have been deleted.
        """
        self.client.login(username="user", password="userpass")
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "Deleted Post")

    def test_order_of_stream(self):
        """
        As an author, I want my "stream" page to be sorted with the most recent posts first.
        """
        older_post = Post.objects.create(
            id=uuid.uuid4(),
            author=self.other_author,
            text="Older Public Post",
            visibility="PUBLIC",
            content_type="text/plain"
        )
        # Delay to make sure created at different times
        time.sleep(0.1)
        newer_post = Post.objects.create(
            id=uuid.uuid4(),
            author=self.other_author,
            text="Newer Public Post",
            visibility="PUBLIC",
            content_type="text/plain"
        )
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        
        self.assertContains(response, "Older Public Post")
        self.assertContains(response, "Newer Public Post")

        content = response.content.decode("utf-8")
        post_newer = content.index("Newer Public Post")
        post_older = content.index("Older Public Post")
        self.assertTrue(post_newer < post_older,
                        "The newer post should appear before the older post.")

