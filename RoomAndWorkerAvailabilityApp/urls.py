from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.conf.urls import include
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.conf import settings
app_name = "availability"
urlpatterns = [
    path("register/", views.register, name="register_worker"),
    path("login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("", views.worker_list, name="workers_list"),
    path("worker/<int:pk>/confirm-status/",views.confirm_worker_status,name="confirm_worker_status",),
    path("worker/<int:pk>/change-status/",views.change_worker_status,name="change_worker_status",),
    path("absence-details/<int:pk>/",views.show_absence_details,name="absence_details"),
    path("rooms/",views.rooms_list,name="rooms_list"),
    path("rooms/<int:pk>/",views.show_room_add_info,name="room_details"),
    path("rules/",views.rules_list,name="rules_list"),
]