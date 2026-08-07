from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.http import HttpResponseForbidden

from .models import Worker
from .forms import AddWorkerForm, ChangeStatusForm

def register(request):
    if request.method == "POST":
        form = AddWorkerForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect("availability:worker_list")

    else:
        form = AddWorkerForm()

    return render(
        request,
        "registration/register.html",
        {"form": form},
    )

@login_required
def worker_list(request):

    first_name_query = request.GET.get("first_name", "").strip()
    last_name_query = request.GET.get("last_name", "").strip()
    departments_query=request.GET.get("department", "").strip()
    positions_query=request.GET.get("position", "").strip()
    sort_query = request.GET.get("sort", "name_asc").strip()

    workers = Worker.objects.all()

    if first_name_query:
        workers = workers.filter(first_name__icontains=first_name_query)
    if last_name_query:
        workers = workers.filter(last_name__icontains=last_name_query)
    if departments_query:
        workers = workers.filter(department=departments_query)
    if positions_query:
        workers = workers.filter(position=positions_query)
    if sort_query == "name_desc":
        workers = workers.order_by("-first_name", "-last_name")
    else:
        workers = workers.order_by("first_name", "last_name")

    return render(
        request,
      "showing_data/list_workers.html",
      {
       "workers": workers,
       "first_name_query": first_name_query,
       "last_name_query": last_name_query,
       "departments_query": departments_query,
       "positions_query": positions_query,
       "sort_query": sort_query,
       "positions_classes":Worker.POSITIONS,
       "departments_classes":Worker.DEPARTMENTS,
       }
                  )

@login_required
def change_worker_status(request):
    if request.method == "POST":
        form=ChangeStatusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("availability:worker_list")
    else:
        form = ChangeStatusForm()
    return render(
        request,
        "modify_worker/change_status.html",
        context={"form": form},
    )