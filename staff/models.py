from django.db import models


class Staff(models.Model):

    ROLE_CHOICES = [
        ("Manager", "Manager"),
        ("Reception", "Reception"),
        ("Trainer", "Trainer"),
    ]

    full_name = models.CharField(max_length=100)

    phone = models.CharField(max_length=15)

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default="Reception"
    )

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.full_name