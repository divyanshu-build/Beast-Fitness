from django.urls import path
from . import views

urlpatterns = [
    path("", views.member_list, name="members"),
    path("view/<int:id>/", views.view_member, name="view_member"),
    path("edit/<int:id>/", views.edit_member, name="edit_member"),
    path("delete/<int:id>/", views.delete_member, name="delete_member"),
]