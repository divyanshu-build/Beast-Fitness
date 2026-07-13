from django.db import models
from members.models import Member
from datetime import timedelta
from django.utils import timezone


class Payment(models.Model):

    PAYMENT_MODE = [
        ("Cash", "Cash"),
        ("UPI", "UPI"),
    ]

    member = models.ForeignKey(
        Member,
        on_delete=models.CASCADE
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    payment_mode = models.CharField(
        max_length=10,
        choices=PAYMENT_MODE
    )

    payment_date = models.DateField(
        default=timezone.now
    )

    next_due_date = models.DateField(
        blank=True,
        null=True
    )

    def save(self, *args, **kwargs):

        if self.member.membership == "Monthly":
            self.next_due_date = self.payment_date + timedelta(days=30)

        elif self.member.membership == "Quarterly":
            self.next_due_date = self.payment_date + timedelta(days=90)

        elif self.member.membership == "Half-Yearly":
            self.next_due_date = self.payment_date + timedelta(days=180)

        elif self.member.membership == "Yearly":
            self.next_due_date = self.payment_date + timedelta(days=365)

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.member.full_name} - ₹{self.amount}"