from django.test import TestCase, Client
from django.urls import reverse
import time, threading, uuid, base64
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from social_distribution.models import Author, Post

class RateLimitingTestCase(TestCase):
    def test_rate_limiting(self):
        # Create a client to make requests
        client = Client()

        time.sleep(60)
        
        # Make 100 requests to the all auhtors view
        for _ in range(100):
            response = client.get(reverse('get_authors'))
            self.assertEqual(response.status_code, 200)

        # Make a 101st request to the all auhtors view
        response = client.get(reverse('get_authors'))
        self.assertEqual(response.status_code, 429)  # Rate limit exceeded

    def test_rate_limiting_reset(self):
        # Create a client to make requests
        client = Client()

        time.sleep(60)
        
        # Make 100 requests to the all auhtors view
        for _ in range(100):
            response = client.get(reverse('get_authors'))
            self.assertEqual(response.status_code, 200)

        # Wait for 1 minute to allow the rate limit to reset   
        time.sleep(60)

        # Make another request to the all auhtors view
        response = client.get(reverse('get_authors'))
        self.assertEqual(response.status_code, 200)  # Rate limit reset
        
class MaliciousInputTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        
        # Create user
        self.user = User.objects.create_user(username="testuser", password="testpass")

        # Create author
        self.author = Author.objects.create(
            id=uuid.uuid4(),
            username="testuser",
            display_name="Test User",
            github="https://github.com/testuser",
            profile_image=None,
            host="http://127.0.0.1:8000"
        )

        # Link users to authors AFTER creation
        self.author.user = self.user
        self.author.save()

        # Create posts
        self.public_post = Post.objects.create(
            id=uuid.uuid4(),
            author=self.author,
            content="<script>alert('XSS');</script>",
            visibility="PUBLIC"
        )    
        
    def test_non_standard_input(self):
        malicious_payload = {
            "content": "<script>alert('XSS');</script>",  # XSS attempt
            "visibility": "'; DROP TABLE users; --",      # SQL Injection
            "content_type": "application/x-httpd-php"    # Unexpected MIME type
        }
        
        url = reverse("posts_detail", args=[self.author.id, self.public_post.id])
        response = self.client.post(url, data=malicious_payload, content_type='application/json')
        
        self.assertEqual(response.status_code, 405)  # Should not allow
        self.assertNotEqual(response.status_code, 200)  # Should not allow
        self.assertNotEqual(response.status_code, 201)  # Should not create resource
        self.assertNotEqual(response.status_code, 500)  # App should handle it gracefully
        

class ImageUploadTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        
        # Create user
        self.user = User.objects.create_user(username="testuser", password="testpass")

        # Create author
        self.author = Author.objects.create(
            id=uuid.uuid4(),
            username="testuser",
            display_name="Test User",
            github="https://github.com/testuser",
            profile_image=None,
            host="http://127.0.0.1:8000"
        )

        # Link users to authors AFTER creation
        self.author.user = self.user
        self.author.save()
        
        self.image_post = Post.objects.create(
            id=uuid.uuid4(),
            author=self.author,
            content=base64.b64encode(b"fake_image_data").decode("utf-8"),
            visibility="PUBLIC",
            content_type="image/jpeg;base64"
        )

    def test_valid_image_formats(self):
        """Test that JPG, JPEG, and PNG are accepted."""
        url = reverse("get_post_image", args=[self.author.id, self.image_post.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response["Content-Type"], "image/jpeg")
            
class OverloadTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('get_authors')

    def make_requests(self):
        for _ in range(50):  # Send 50 rapid requests
            response = self.client.get(self.url)
            if response.status_code == 429:  # Check if rate limit is triggered
                break

    def test_system_overload(self):
        threads = []
        for _ in range(10):  # Launch 10 parallel threads
            thread = threading.Thread(target=self.make_requests)
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 429)  # Expect rate limit to activate

class CodeInjectionTestCase(TestCase):
    
    def setUp(self):
        self.client = APIClient()
        
        # Create user
        self.user = User.objects.create_user(username="testuser", password="testpass")

        # Create author
        self.author = Author.objects.create(
            id=uuid.uuid4(),
            username="testuser",
            display_name="Test User",
            github="https://github.com/testuser",
            profile_image=None,
            host="http://127.0.0.1:8000"
        )

        # Link users to authors AFTER creation
        self.author.user = self.user
        self.author.save()

        # Create posts
        self.public_post = Post.objects.create(
            id=uuid.uuid4(),
            author=self.author,
            content="print('Hello, World!')",
            visibility="PUBLIC"
        )    

    def test_code_payload(self):
        url = reverse("posts_detail", args=[self.author.id, self.public_post.id])
        response = self.client.get(url)  # No authentication needed
        
        self.assertNotEqual(response.status_code, 500)  # Should not crash
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["content"], "print('Hello, World!')")
        