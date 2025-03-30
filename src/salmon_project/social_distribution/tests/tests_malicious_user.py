from django.test import TestCase, Client
from django.urls import reverse

class RateLimitingTestCase(TestCase):
    def test_rate_limiting(self):
        # Create a client to make requests
        client = Client()

        # Make 100 requests to the all auhtors view
        for _ in range(1000):
            response = client.get(reverse('get_authors'))
            self.assertEqual(response.status_code, 200)

        # Make a 1001st request to the all auhtors view
        response = client.get(reverse('get_authors'))
        self.assertEqual(response.status_code, 429)  # Rate limit exceeded

    def test_rate_limiting_reset(self):
        # Create a client to make requests
        client = Client()

        # Make 100 requests to the all auhtors view
        for _ in range(1000):
            response = client.get(reverse('get_authors'))
            self.assertEqual(response.status_code, 200)

        # Wait for 1 minute to allow the rate limit to reset
        import time
        time.sleep(60)

        # Make another request to the all auhtors view
        response = client.get(reverse('get_authors'))
        self.assertEqual(response.status_code, 200)  # Rate limit reset