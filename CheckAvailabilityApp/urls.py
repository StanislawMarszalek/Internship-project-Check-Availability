### Copyright to django-scheduler app
"""
Copyright (c) 2008-2017, Tony Hauber
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are
met:

    * Redistributions of source code must retain the above copyright
      notice, this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above
      copyright notice, this list of conditions and the following
      disclaimer in the documentation and/or other materials provided
      with the distribution.
    * Neither the name of the author nor the names of other
      contributors may be used to endorse or promote products derived
      from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

### Link to 'django-scheduler' app
### https://github.com/llazzaro/django-scheduler?tab=BSD-3-Clause-1-ov-file
from django.contrib import admin
from django.urls import include, path
from RoomAndWorkerAvailabilityApp import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("RoomAndWorkerAvailabilityApp.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("register/", views.register, name="register"),
    path("password-reset/", auth_views.PasswordResetView.as_view(
            template_name="registration/password_reset_form.html"
        ), name="password_reset"),

    path("password-reset/done/", auth_views.PasswordResetDoneView.as_view(
        template_name="registration/password_reset_done.html"
    ), name="password_reset_done"),

    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(
        template_name="registration/password_reset_confirm.html"
    ), name="password_reset_confirm"),

    path("reset/done/", auth_views.PasswordResetCompleteView.as_view(
        template_name="registration/password_reset_complete.html"
    ), name="password_reset_complete"),
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
    path('schedule/', include('schedule.urls')),
]
