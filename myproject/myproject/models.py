from django.db import models


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
