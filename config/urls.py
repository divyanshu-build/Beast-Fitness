from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", include("dashboard.urls")),

    path("members/", include("members.urls")),

    path("payments/", include("payments.urls")),

    path("attendance/", include("attendance.urls")),
]