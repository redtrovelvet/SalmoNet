from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from social_distribution.models import NodeInfo, RemoteNode, User, Author
import uuid
from django.conf import settings

class NodeManagementTests(TestCase):
    def setUp(self):
        self.local_node = settings.BASE_URL
        self.remote_node = "http://remote-node.com"
        self.username = "testuser"
        self.password = "testpass"
        self.client = APIClient()
        # Create a superuser for testing
        self.user = User.objects.create_user(
            username="admin",
            password="adminpass",
            is_superuser=True,
            is_staff=True,
        )
        # make a superuser author
        self.author = Author.objects.create(
            id=uuid.uuid4(),
            username="admin",
            display_name="Admin User",
            host=self.local_node,
        )
        self.author.user = self.user
        
    def test_set_node_info(self):
        """
        Test for setting local node information.
        api/set_node_info/
        """
        # Log in as the superuser
        self.client.login(username="admin", password="adminpass")
        response = self.client.post(
            reverse("set_node_info"),
            data={
                "username": self.username,
                "password": self.password,
            },
        )
        self.assertEqual(response.status_code, 201)
        local_node = NodeInfo.objects.get(host=self.local_node)
        self.assertEqual(local_node.username, self.username)
        self.assertEqual(local_node.password, self.password)
        self.assertEqual(local_node.host, self.local_node)        


    def test_add_remote_node(self):
        """
        Test for adding a remote node to the db.
        api/add_remote_node/
        """
        # Log in as the superuser
        self.client.login(username="admin", password="adminpass")
        response = self.client.post(
            reverse("add_remote_node"),
            data={
                "host": self.remote_node,
                "username": self.username,
                "password": self.password,
            },
        )
        self.assertEqual(response.status_code, 201)
        remote_node = RemoteNode.objects.get(host=self.remote_node)
        self.assertEqual(remote_node.host, self.remote_node)
        self.assertEqual(remote_node.username, self.username)
        self.assertEqual(remote_node.password, self.password)
        self.assertEqual(remote_node.outgoing, True)
        self.assertEqual(remote_node.incoming, False)

    def test_connect_node(self):
        """
        Test for connecting to a remote node.
        api/connect/
        """
        # Log in as the superuser
        self.client.login(username="admin", password="adminpass")
        response = self.client.post(
            reverse("set_node_info"),
            data={
                "username": self.username,
                "password": self.password,
            },
        )
        response = self.client.post(
            reverse("connect_node"),
            HTTP_ORIGIN=self.remote_node,
            data={
                "username": self.username,
                "password": self.password,
            },
        )
        self.assertEqual(response.status_code, 201)
        remote_node = RemoteNode.objects.get(host=self.remote_node)
        self.assertEqual(remote_node.host, self.remote_node)
        self.assertEqual(remote_node.outgoing, False)
        self.assertEqual(remote_node.incoming, True)

    
    def test_remove_connection(self):
        """
        Test for removing a connection to a remote node.
        api/remove_connection/
        """
        self.client.login(username="admin", password="adminpass")
        # Create a remote node to remove
        RemoteNode.objects.create(
            host=self.remote_node,
            username=self.username,
            password=self.password,
            outgoing=True,
            incoming=False,
        )
        self.assertEqual(RemoteNode.objects.count(), 1, "One remote nodes should exist")
        response = self.client.post(
            reverse("remove_connection"),
            data={
                "host": self.remote_node,
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(RemoteNode.objects.get(host=self.remote_node).outgoing, False)
            

    def test_connect_external(self):
        """
        Test for connecting to an external node from a different group.
        api/connect_external/
        """
        self.client.login(username="admin", password="adminpass")
        request = self.client.post(
            reverse("connect_external"),
            data={
                "host": self.remote_node,
                "username": self.username,
                "password": self.password,
            },
        )
        self.assertEqual(request.status_code, 201)
        remote_node = RemoteNode.objects.get(host=self.remote_node)
        self.assertEqual(remote_node.host, self.remote_node)
        self.assertEqual(remote_node.username, self.username)
        self.assertEqual(remote_node.password, self.password)
        self.assertEqual(remote_node.outgoing, True)
        self.assertEqual(remote_node.incoming, True)