from django.contrib import admin
from .models import Staff


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "phone",
        "role",
        "is_active",
    )

    search_fields = (
        "full_name",
        "phone",
    )

    list_filter = (
        "role",
        "is_active",
    )