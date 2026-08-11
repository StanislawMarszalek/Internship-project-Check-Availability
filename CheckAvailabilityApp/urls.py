"""
URL configuration for CheckAvailabilityApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from RoomAndWorkerAvailabilityApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("RoomAndWorkerAvailabilityApp.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("register/", views.register, name="register"),
    path(
        "schedule/event/create/<slug:calendar_slug>/",
        views.CustomCreateEventView.as_view(),
        name="calendar_create_event",
    ),
    path(
        "schedule/event/delete/<int:event_id>/",
        views.CustomDeleteEventView.as_view(),
        name="delete_event",
    ),
    path(
        "schedule/event/edit/<slug:calendar_slug>/<int:event_id>/",
        views.CustomEditEventView.as_view(),
        name="edit_event",
    ),
    path(
            "schedule/fullcalendar/<slug:calendar_slug>/",
            views.MyFullCalendarView.as_view(),
            name="my_fullcalendar",
        ),

path("schedule/", include("schedule.urls")),
    path('schedule/', include('schedule.urls')),
]
