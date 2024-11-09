from django.urls import path
from . import views

urlpatterns = [
    path("crear/", views.crear_avatar, name="crear_avatar"),
]
