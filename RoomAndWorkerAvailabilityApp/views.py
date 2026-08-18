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



from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.http import HttpResponseForbidden
from django.views.generic import TemplateView
from schedule.models import Event, Calendar, Rule

from .models import Worker, Room
from .forms import AddWorkerForm, ChangeStatusForm
from schedule.views import CreateEventView
from .forms import AddEventForm

from schedule.views import DeleteEventView
from django.shortcuts import redirect
from schedule.views import EditEventView

from django.contrib.auth.mixins import LoginRequiredMixin

#TODO uporzadkowac wszedzie importy

def register(request):
    if request.method == "POST":
        form = AddWorkerForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect("availability:workers_list")

    else:
        form = AddWorkerForm()

    return render(
        request,
        "registration/register.html",
        {"form": form},
    )

@login_required
def worker_list(request):

    username_query=request.GET.get("username", "").strip()
    departments_query=request.GET.get("department", "").strip()
    positions_query=request.GET.get("position", "").strip()
    sort_query = request.GET.get("sort", "name_asc").strip()

    workers = Worker.objects.all()

    if username_query:
        workers=workers.filter(username__icontains=username_query)
    if departments_query:
        workers = workers.filter(department=departments_query)
    if positions_query:
        workers = workers.filter(position=positions_query)
    if sort_query == "name_desc":
        workers = workers.order_by("-username", "-position","-is_present")
    else:
        workers = workers.order_by("username", "position","is_present")

    return render(
        request,
      "showing_data/list_workers.html",
      {
       "workers": workers,
        "username_query":username_query,
       "departments_query": departments_query,
       "positions_query": positions_query,
       "sort_query": sort_query,
       "positions_classes":Worker.POSITIONS,
       "departments_classes":Worker.DEPARTMENTS,
       }
                  )

@login_required
def confirm_worker_status(request, pk):
    worker = get_object_or_404(Worker, pk=pk)
    if worker.username != request.user.username :
        return HttpResponseForbidden(
            "You are NOT the user"
        )
    return render(
        request,
        "modify_worker/confirm_change_status.html",
        {
            "worker": worker,
        },
    )


@login_required
def change_worker_status(request, pk):
    worker = get_object_or_404(Worker, pk=pk)
    if worker.username != request.user.username :
        return HttpResponseForbidden(
            "You are NOT the user"
        )

    if not worker.is_present:
        worker.is_present = True
        worker.save()

        return redirect("availability:workers_list")

    if request.method == "POST":
        worker.is_present = False

        form = ChangeStatusForm(
            request.POST,
            instance=worker,
        )

        if form.is_valid():
            form.save()
            return redirect("availability:workers_list")

    else:
        form = ChangeStatusForm(instance=worker)

    return render(
        request,
        "modify_worker/change_worker_status.html",
        {
            "form": form,
            "worker": worker,
        },
    )

@login_required
def show_absence_details(request,pk):
    worker = get_object_or_404(Worker, pk=pk)
    start=worker.start_of_absence
    end=worker.end_of_absence
    reason=worker.reason_of_absence

    return render(
        request,
        "showing_data/absence_details.html",
        context={
            "start": start,
            "end": end,
            "reason": reason,
        }
    )

@login_required
def rooms_list(request):

    room_number_query = request.GET.get("id", "").strip()
    room_name_query = request.GET.get("room_name", "").strip()
    room_floor_query = request.GET.get("room_floor", "").strip()
    additional_room_info_query = request.GET.get("additional_room_info", "").strip()
    building_name_query = request.GET.get("building_name", "").strip()
    sort_query = request.GET.get("sort", "name_asc").strip()

    rooms = Room.objects.all()

    if room_number_query:
        rooms = rooms.filter(id=room_number_query)

    if room_name_query:
        rooms = rooms.filter(room_name__icontains=room_name_query)

    if room_floor_query:
        rooms = rooms.filter(room_floor=room_floor_query)

    if additional_room_info_query:
        rooms = rooms.filter(additional_room_info__icontains=additional_room_info_query)

    if building_name_query:
        rooms = rooms.filter(building_name__icontains=building_name_query)

    if sort_query == "name_desc":
        rooms = rooms.order_by("-id", "-room_name")
    else:
        rooms = rooms.order_by("id", "room_name")

    return render(
        request,
        "showing_data/list_rooms.html",
        {
            "rooms": rooms,
            "room_number_query": room_number_query,
            "room_name_query": room_name_query,
            "room_floor_query": room_floor_query,
            "additional_room_info_query": additional_room_info_query,
            "building_name_query": building_name_query,
            "room_floors":Room.FLOORS,

        }
    )

@login_required
def show_room_add_info(request,pk):
    room = get_object_or_404(Room, pk=pk)
    room_number=room.id
    room_description=room.additional_room_info if room.additional_room_info else "No additional info"
    return render(
        request,
        "showing_data/additional_info.html",
        context={
            "room_number": room_number ,
            "room_description": room_description,
        }
    )


class CustomCreateEventView(LoginRequiredMixin, CreateEventView):
    form_class = AddEventForm

    def form_valid(self, form):

        calendar = Calendar.objects.get(
            slug=self.kwargs["calendar_slug"]
        )

        start = form.cleaned_data["start"]
        end = form.cleaned_data["end"]

        overlapping_events = Event.objects.filter(
            calendar=calendar,
            start__lt=end,
            end__gt=start,
        )

        if overlapping_events.exists():
            form.add_error(
                None,
                "Events cannot overlap."
            )
            return self.form_invalid(form)

        form.instance.calendar = calendar

        return super().form_valid(form)

class CustomDeleteEventView(LoginRequiredMixin, DeleteEventView):

    def dispatch(self,request,*args,**kwargs):
        self.object = self.get_object()
        if self.object.creator != request.user and not request.user.is_superuser:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        if "cancel" in request.POST:
            return redirect(
                "my_fullcalendar",
                calendar_slug=self.object.calendar.slug
            )
        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        return redirect(
            "fullcalendar",
            calendar_slug=self.object.calendar.slug
        ).url


class CustomEditEventView(LoginRequiredMixin, EditEventView):
    form_class = AddEventForm

    def dispatch(self,request,*args,**kwargs):
        self.object = self.get_object()
        if self.object.creator != request.user and not request.user.is_superuser:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return redirect(
            "fullcalendar",
            calendar_slug=self.object.calendar.slug
        ).url

class MyFullCalendarView(LoginRequiredMixin, TemplateView):
    template_name = "schedule/fullcalendar.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["calendar_slug"] = self.kwargs["calendar_slug"]
        return context

@login_required
def rules_list(request):
    if not request.user.is_superuser:
        return HttpResponseForbidden(
            "You are NOT the admin"
        )
    rules = Rule.objects.all()

    name_query=request.GET.get("name", "").strip()
    description_query=request.GET.get("description", "").strip()
    frequency_query=request.GET.get("frequency", "").strip()
    sort_query = request.GET.get("sort", "name_asc").strip()

    if name_query:
        rules = rules.filter(name__icontains=name_query)
    if description_query:
        rules = rules.filter(description__icontains=description_query)
    if frequency_query:
        rules = rules.filter(frequency__icontains=frequency_query)

    if sort_query == "name_desc":
        rules = rules.order_by("-name", "-frequency")
    else:
        rules = rules.order_by("name", "frequency")

    return render(
        request,
        template_name="showing_data/calendar_rules.html",
        context={
            "rules":rules,
            "name_query":name_query,
            "description_query":description_query,
            "frequency_query":frequency_query,
            "sort_query":sort_query
        }
    )