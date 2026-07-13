from django.contrib import admin
from .models import Attendance


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):

    list_display = (
        "member",
        "attendance_date",
        "entry_time",
        "exit_time",
        "status",
    )

    list_filter = (
        "attendance_date",
        "status",
    )

    search_fields = (
        "member__full_name",
        "member__member_id",
    )