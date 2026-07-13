from django.db import models
from django.db.models import Max


class Member(models.Model):

    GENDER_CHOICES = [
        ("Male", "Male"),
        ("Female", "Female"),
    ]

    MEMBERSHIP_CHOICES = [
        ("Monthly", "Monthly"),
        ("Quarterly", "Quarterly"),
        ("Half-Yearly", "Half-Yearly"),
        ("Yearly", "Yearly"),
    ]

    member_id = models.CharField(max_length=10, unique=True, blank=True)
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    age = models.PositiveIntegerField()
    address = models.TextField()
    membership = models.CharField(max_length=20, choices=MEMBERSHIP_CHOICES)
    joining_date = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.member_id:
            last = Member.objects.aggregate(Max("id"))
            last_id = last["id__max"] or 0
            self.member_id = f"BF{last_id + 1:04d}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.member_id} - {self.full_name}"