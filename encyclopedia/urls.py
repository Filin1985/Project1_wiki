from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.title, name="title"),
    path("newpage", views.newPage, name="newpage"),
    path("wiki/<str:title>/edit", views.edit, name="edit")
]
