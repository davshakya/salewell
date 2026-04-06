from django.test import TestCase
from django.urls import reverse

from .models import Lead


class StorefrontTests(TestCase):
    def test_homepage_renders_storefront_content(self):
        response = self.client.get(reverse("index"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Shop Women")
        self.assertContains(response, "Request Catalogue")

    def test_valid_enquiry_is_saved(self):
        response = self.client.post(
            reverse("index"),
            {
                "name": "Asha",
                "email": "asha@example.com",
                "interest": Lead.WOMEN,
                "message": "Looking for weekend outfits in neutral tones.",
            },
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response["Location"], f"{reverse('index')}#contact")
        self.assertEqual(Lead.objects.count(), 1)
