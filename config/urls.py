from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth import logout
from django.shortcuts import redirect


def logout_view(request):
    logout(request)
    return redirect("login")


urlpatterns = [

    # Login
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="login.html"
        ),
        name="login",
    ),

    # Logout
    path(
        "logout/",
        logout_view,
        name="logout",
    ),

    # Django Admin
    path("admin/", admin.site.urls),

    # Dashboard
    path("", include("dashboard.urls")),

    # Members
    path("members/", include("members.urls")),

    # Payments
    path("payments/", include("payments.urls")),

    # Attendance
    path("attendance/", include("attendance.urls")),

    # Staff
    path("staff/", include("staff.urls")),
]