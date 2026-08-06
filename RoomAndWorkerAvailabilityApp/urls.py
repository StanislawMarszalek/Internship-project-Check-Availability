from django.urls import path
from . import views

app_name = "availability"
urlpatterns = [
    path("", views.register, name="register_worker"),
]