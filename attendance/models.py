from django.db import models
from members.models import Member


class Attendance(models.Model):

    STATUS_CHOICES = [
        ("Inside", "Inside"),
        ("Exited", "Exited"),
        ("Auto Exit", "Auto Exit"),
    ]

    member = models.ForeignKey(
        Member,
        on_delete=models.CASCADE
    )

    attendance_date = models.DateField(auto_now_add=True)

    entry_time = models.DateTimeField(auto_now_add=True)

    exit_time = models.DateTimeField(
        null=True,
        blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Inside"
    )

    def __str__(self):
        return f"{self.member.full_name} - {self.attendance_date}"