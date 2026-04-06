import uuid

from django.db import models
from django.utils import timezone


class Lead(models.Model):
    WOMEN = "women"
    MEN = "men"
    BOTH = "both"
    OCCASION = "occasion"

    INTEREST_CHOICES = [
        (WOMEN, "Women"),
        (MEN, "Men"),
        (BOTH, "Women and Men"),
        (OCCASION, "Festive or Occasion Wear"),
    ]

    name = models.CharField(max_length=120)
    email = models.EmailField()
    interest = models.CharField(max_length=20, choices=INTEREST_CHOICES)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"{self.name} - {self.get_interest_display()}"


class Order(models.Model):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    SHIPPED = "shipped"
    DELIVERED = "delivered"

    STATUS_CHOICES = [
        (PENDING, "Pending"),
        (CONFIRMED, "Confirmed"),
        (SHIPPED, "Shipped"),
        (DELIVERED, "Delivered"),
    ]

    order_number = models.CharField(max_length=24, unique=True, editable=False)
    customer_name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address_line1 = models.CharField(max_length=255)
    address_line2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=120)
    state = models.CharField(max_length=120)
    postal_code = models.CharField(max_length=20)
    delivery_area = models.CharField(max_length=120, default="India")
    notes = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=PENDING)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    shipping_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def save(self, *args, **kwargs):
        if not self.order_number:
            stamp = timezone.now().strftime("%Y%m%d")
            self.order_number = f"SW-{stamp}-{uuid.uuid4().hex[:6].upper()}"
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.order_number} - {self.customer_name}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product_slug = models.CharField(max_length=120)
    product_name = models.CharField(max_length=120)
    category = models.CharField(max_length=20)
    product_type = models.CharField(max_length=80)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    line_total = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        ordering = ["id"]

    def __str__(self) -> str:
        return f"{self.product_name} x {self.quantity}"
