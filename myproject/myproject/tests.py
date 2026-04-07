from django.test import TestCase
from django.urls import reverse

from .models import Lead, Order, OrderItem


class StorefrontTests(TestCase):
    def test_homepage_renders_storefront_content(self):
        response = self.client.get(reverse("index"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Shop Home Systems")
        self.assertContains(response, "Checkout")

    def test_valid_enquiry_is_saved(self):
        response = self.client.post(
            reverse("index"),
            {
                "form_type": "lead",
                "name": "Asha",
                "email": "asha@example.com",
                "interest": Lead.HOME,
                "message": "Need automation for one home tank and a 1 HP pump.",
            },
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response["Location"], f"{reverse('index')}#catalogue-request")
        self.assertEqual(Lead.objects.count(), 1)

    def test_category_and_product_pages_render(self):
        residential_response = self.client.get(reverse("residential"))
        product_response = self.client.get(reverse("product_detail", args=["smart-overflow-guard-mini"]))

        self.assertEqual(residential_response.status_code, 200)
        self.assertContains(residential_response, "solutions available")
        self.assertEqual(product_response.status_code, 200)
        self.assertContains(product_response, "Smart Overflow Guard Mini")

    def test_checkout_creates_order_and_items(self):
        add_response = self.client.post(
            reverse("add_to_cart", args=["smart-overflow-guard-mini"]),
            {"quantity": 2, "next": reverse("cart")},
        )
        self.assertEqual(add_response.status_code, 302)

        response = self.client.post(
            reverse("checkout"),
            {
                "customer_name": "Devendra",
                "email": "dev@example.com",
                "phone": "9999999999",
                "address_line1": "123 Market Road",
                "address_line2": "Near Main Chowk",
                "city": "Orai",
                "state": "Uttar Pradesh",
                "postal_code": "285001",
                "delivery_area": "India",
                "notes": "Single tank setup, 1 HP pump, need installation guidance.",
            },
        )

        self.assertEqual(response.status_code, 302)
        self.assertTrue(response["Location"].startswith(reverse("orders")))
        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(OrderItem.objects.count(), 1)
        self.assertEqual(Order.objects.first().items.first().quantity, 2)
