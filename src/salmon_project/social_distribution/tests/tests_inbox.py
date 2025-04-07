import uuid
import base64
from django.conf import settings
from django.urls import reverse
from django.test import TestCase, override_settings
from rest_framework.test import APIClient
from rest_framework import status
from unittest.mock import patch
from social_distribution import views
from social_distribution.models import Author, Post, Comment, FollowRequest, NodeInfo, RemoteNode

# Dummy response to simulate external HTTP calls from helper functions.
class DummyResponse:
    status_code = 201

@override_settings(BASE_URL="http://localhost")
class RemoteInboxTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Create a local receiver (the target of the inbox).
        self.receiver = Author.objects.create(
            username="local_receiver",
            display_name="Local Receiver",
            is_approved=True
        )
        self.receiver.refresh_from_db()  # Ensure fqid is set (e.g. "http://localhost/api/authors/<id>")

        # Create a remote sender with its fqid set to a remote URL.
        self.remote_sender = Author.objects.create(
            username="remote_sender",
            display_name="Remote Sender",
            is_approved=True
        )
        self.remote_sender.fqid = "http://remote-node/api/authors/111"
        self.remote_sender.save()

        # For testing remote like/comment on local objects, create a local post.
        self.local_post = Post.objects.create(
            author=self.receiver,
            content="Local post content",
            content_type="text/plain",
            visibility="PUBLIC"
        )
        self.local_post.refresh_from_db()  # Its fqid is set to "http://localhost/api/authors/<receiver.id>/posts/<id>"

        # Create a NodeInfo record for Basic Auth.
        self.node_info = NodeInfo.objects.create(
            username="nodeuser",
            password="nodepass",
            host=settings.BASE_URL
        )
        # (Optionally) create a RemoteNode record if your helper functions use it.
        RemoteNode.objects.create(
            host="http://remote-node/api/",
            outgoing=True,
            incoming=True,
            username="remotepostuser",
            password="remotepostpass"
        )

        # Build the inbox URL for the local receiver.
        self.inbox_url = reverse("inbox", args=[self.receiver.id])
        credentials = f"{self.node_info.username}:{self.node_info.password}"
        self.valid_auth = "Basic " + base64.b64encode(credentials.encode()).decode()
        self.invalid_auth = "Basic " + base64.b64encode("bad:creds".encode()).decode()

    # --------------------------
    # Authorized Remote Requests
    # --------------------------
    def test_remote_post_from_remote_author(self):
        """
        A remote author creates a post payload and sends it to a local author's inbox.
        Expect the post to be processed and a 201 response.
        """
        payload = {
            "type": "post",
            "title": "Remote Post Title",
            "id": "http://remote-node/api/authors/111/posts/zzz111",
            "page": "http://remote-node/authors/111/posts/zzz111",
            "description": "Remote post description",
            "contentType": "text/plain",
            "content": "This is remote post content",
            "author": {
                "type": "author",
                "id": self.remote_sender.fqid,
                "host": "http://remote-node/api/",
                "displayName": "Remote Sender",
                "page": "http://remote-node/authors/111",
                "github": "http://github.com/remotesender",
                "profileImage": "http://remote-node/authors/111/image"
            },
            "comments": {"src": []},
            "likes": {"src": []},
            "published": "2015-03-09T13:07:04+00:00",
            "visibility": "PUBLIC"
        }
        response = self.client.post(
            self.inbox_url,
            payload,
            format="json",
            HTTP_AUTHORIZATION=self.valid_auth
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["detail"], "Post and associated objects processed.")

    @patch("social_distribution.views.send_post_to_remote", return_value=DummyResponse())
    def test_remote_like_on_local_post(self, mock_send_post):
        """
        A remote like payload on a local post from a remote author should be processed.
        """
        payload = {
            "type": "like",
            "author": {
                "type": "author",
                "id": self.remote_sender.fqid,
                "host": "http://remote-node/api/",
                "displayName": "Remote Sender",
                "page": "http://remote-node/authors/111",
                "github": "http://github.com/remotesender",
                "profileImage": "http://remote-node/authors/111/image"
            },
            # The like's id is remote, triggering the remote branch.
            "id": "http://remote-node/api/authors/111/liked/" + str(uuid.uuid4()),
            # Object points to the local post's fqid.
            "object": self.local_post.fqid,
            "published": "2015-03-09T13:07:04+00:00"
        }
        response = self.client.post(
            self.inbox_url,
            payload,
            format="json",
            HTTP_AUTHORIZATION=self.valid_auth
        )
        self.assertIn(response.status_code, [status.HTTP_200_OK, status.HTTP_201_CREATED])
        self.assertIn("like", response.data["detail"].lower())
        self.assertIn("notification", response.data)
        mock_send_post.assert_called()

    @patch("social_distribution.views.send_post_to_remote", return_value=DummyResponse())
    def test_remote_comment_on_local_post(self, mock_send_post):
        """
        A remote comment payload on a local post from a remote author should be processed.
        """
        payload = {
            "type": "comment",
            "author": {
                "type": "author",
                "id": self.remote_sender.fqid,
                "host": "http://remote-node/api/",
                "displayName": "Remote Sender",
                "page": "http://remote-node/authors/111",
                "github": "http://github.com/remotesender",
                "profileImage": "http://remote-node/authors/111/image"
            },
            "comment": "This is a remote comment on a local post",
            "contentType": "text/markdown",
            "published": "2015-03-09T13:07:04+00:00",
            "id": "http://remote-node/api/authors/111/commented/" + str(uuid.uuid4()),
            # "post" points to the local post's fqid.
            "post": self.local_post.fqid,
            "likes": {"src": []}
        }
        response = self.client.post(
            self.inbox_url,
            payload,
            format="json",
            HTTP_AUTHORIZATION=self.valid_auth
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["detail"], "Comment and embedded likes stored.")
        self.assertIn("notification", response.data)
        mock_send_post.assert_called()

    @patch("social_distribution.views.send_object", return_value=DummyResponse())
    def test_remote_like_on_local_comment(self, mock_send_obj):
        """
        A remote like payload on a local comment from a remote author should be processed.
        """
        # Create a local comment on the local post.
        local_comment = Comment.objects.create(
            post=self.local_post,
            author=self.receiver,
            comment="Local comment to be liked",
            content_type="text/plain"
        )
        local_comment.refresh_from_db()  # fqid becomes "http://localhost/api/authors/<receiver.id>/commented/<id>"
        payload = {
            "type": "like",
            "author": {
                "type": "author",
                "id": self.remote_sender.fqid,
                "host": "http://remote-node/api/",
                "displayName": "Remote Sender",
                "page": "http://remote-node/authors/111",
                "github": "http://github.com/remotesender",
                "profileImage": "http://remote-node/authors/111/image"
            },
            # Remote like object id.
            "id": "http://remote-node/api/authors/111/liked/" + str(uuid.uuid4()),
            # Object points to the local comment's fqid.
            "object": local_comment.fqid,
            "published": "2015-03-09T13:07:04+00:00"
        }
        response = self.client.post(
            self.inbox_url,
            payload,
            format="json",
            HTTP_AUTHORIZATION=self.valid_auth
        )
        self.assertIn(response.status_code, [status.HTTP_200_OK, status.HTTP_201_CREATED])
        self.assertIn("comment like", response.data["detail"].lower())
        mock_send_obj.assert_called()

    # --------------------------
    # Unauthorized Remote Requests
    # --------------------------
    def test_remote_post_without_auth(self):
        """
        A remote post payload without a Basic Auth header should be rejected (401).
        """
        payload = {
            "type": "post",
            "title": "Unauthorized Remote Post",
            "id": "http://remote-node/api/authors/111/posts/zzz111",
            "page": "http://remote-node/authors/111/posts/zzz111",
            "description": "Unauthorized remote post description",
            "contentType": "text/plain",
            "content": "Unauthorized remote post content",
            "author": {
                "type": "author",
                "id": self.remote_sender.fqid,
                "host": "http://remote-node/api/",
                "displayName": "Remote Sender",
                "page": "http://remote-node/authors/111",
                "github": "http://github.com/remotesender",
                "profileImage": "http://remote-node/authors/111/image"
            },
            "comments": {"src": []},
            "likes": {"src": []},
            "published": "2015-03-09T13:07:04+00:00",
            "visibility": "PUBLIC"
        }
        response = self.client.post(self.inbox_url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_remote_like_without_auth(self):
        """
        A remote like payload on a local post without a Basic Auth header should return 401.
        """
        payload = {
            "type": "like",
            "author": {
                "type": "author",
                "id": self.remote_sender.fqid,
                "host": "http://remote-node/api/",
                "displayName": "Remote Sender",
                "page": "http://remote-node/authors/111",
                "github": "http://github.com/remotesender",
                "profileImage": "http://remote-node/authors/111/image"
            },
            "id": "http://remote-node/api/authors/111/liked/" + str(uuid.uuid4()),
            "object": self.local_post.fqid,
            "published": "2015-03-09T13:07:04+00:00"
        }
        response = self.client.post(self.inbox_url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_remote_comment_without_auth(self):
        """
        A remote comment payload on a local post without a Basic Auth header should return 401.
        """
        payload = {
            "type": "comment",
            "author": {
                "type": "author",
                "id": self.remote_sender.fqid,
                "host": "http://remote-node/api/",
                "displayName": "Remote Sender",
                "page": "http://remote-node/authors/111",
                "github": "http://github.com/remotesender",
                "profileImage": "http://remote-node/authors/111/image"
            },
            "comment": "Unauthorized remote comment on local post",
            "contentType": "text/markdown",
            "published": "2015-03-09T13:07:04+00:00",
            "id": "http://remote-node/api/authors/111/commented/" + str(uuid.uuid4()),
            "post": self.local_post.fqid,
            "likes": {"src": []}
        }
        response = self.client.post(self.inbox_url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
