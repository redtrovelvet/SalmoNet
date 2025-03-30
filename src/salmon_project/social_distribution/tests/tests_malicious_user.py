from django.test import TestCase, Client
from django.urls import reverse

class RateLimitingTestCase(TestCase):
    def test_rate_limiting(self):
        # Create a client to make requests
        client = Client()

        # Make 5 requests to the inbox view
        for _ in range(10):
            response = client.post(reverse('inbox'))
            self.assertEqual(response.status_code, 201)

        # Make a 6th request to the inbox view
        response = client.post(reverse('inbox'))
        self.assertEqual(response.status_code, 429)  # Rate limit exceeded

    def test_rate_limiting_reset(self):
        # Create a client to make requests
        client = Client()

        # Make 5 requests to the inbox view
        for _ in range(10):
            response = client.post(reverse('inbox'))
            self.assertEqual(response.status_code, 201)

        # Wait for 1 minute to allow the rate limit to reset
        import time
        time.sleep(60)

        # Make another request to the inbox view
        response = client.post(reverse('inbox'))
        self.assertEqual(response.status_code, 201)  # Rate limit reset