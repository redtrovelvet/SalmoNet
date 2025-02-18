#references:
#https://stackoverflow.com/questions/26298821/django-testing-model-with-imagefield#26307916

from django.test import TestCase
from django.urls import reverse
from .models import Author
import uuid
from django.core.files.uploadedfile import SimpleUploadedFile


# Create your tests here.
class AuthorTests(TestCase):

    def setUp(self):
        self.image = SimpleUploadedFile("test_image.jpg", b"fake_image_data", content_type="image/jpeg")
        self.author = Author.objects.create(
            username = "testuser",
            display_name = "Test User",
            github = "https://github.com/testuser",
            profile_image = self.image,
        )
    
    def test_get_author(self):
        response = self.client.get(reverse('get_author', args=[self.author.id]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['username'], "testuser")

    def test_update_author(self):
        response = self.client.post(reverse('update_author', args=[self.author.id]) , {
            "display_name":"Updated User",
            "github": "https://github.com/updateduser"
        }, content_type="application/json")
        self.assertEqual(response.status_code, 200)
        self.author.refresh_from_db()
        self.assertEqual(self.author.display_name, "Updated User")