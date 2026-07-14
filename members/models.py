from django.db import models
from django.db.models import Max
from datetime import timedelta
from django.utils import timezone


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

    member_id = models.CharField(
        max_length=10,
        unique=True,
        blank=True
    )

    full_name = models.CharField(max_length=100)

    phone = models.CharField(max_length=15)

    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES
    )

    age = models.PositiveIntegerField()

    address = models.TextField()

    membership = models.CharField(
        max_length=20,
        choices=MEMBERSHIP_CHOICES
    )

    joining_date = models.DateField(
        auto_now_add=True
    )

    next_due_date = models.DateField(
        null=True,
        blank=True
    )

    fee_status = models.CharField(
        max_length=10,
        default="Paid"
    )

    def save(self, *args, **kwargs):

        # Auto Member ID
        if not self.member_id:
            last = Member.objects.aggregate(Max("id"))
            last_id = last["id__max"] or 0
            self.member_id = f"BF{last_id + 1:04d}"

        # joining_date save hone se pehle None hoti hai
        join_date = self.joining_date or timezone.localdate()

        # Next Due Date
        if not self.next_due_date:

            if self.membership == "Monthly":
                self.next_due_date = join_date + timedelta(days=30)

            elif self.membership == "Quarterly":
                self.next_due_date = join_date + timedelta(days=90)

            elif self.membership == "Half-Yearly":
                self.next_due_date = join_date + timedelta(days=180)

            elif self.membership == "Yearly":
                self.next_due_date = join_date + timedelta(days=365)

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.member_id} - {self.full_name}"