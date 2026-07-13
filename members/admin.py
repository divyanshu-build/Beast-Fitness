from django.contrib import admin
from .models import Member


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):

    list_display = (
        "member_id",
        "full_name",
        "phone",
        "membership",
        "joining_date",
    )

    search_fields = (
        "member_id",
        "full_name",
        "phone",
    )

    list_filter = (
        "membership",
    )