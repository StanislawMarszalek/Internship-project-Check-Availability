from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.http import HttpResponseForbidden

from .models import Worker
from .forms import AddWorkerForm

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
    workers = Worker.objects.all()

    return render(request,
                  "showing_data/list_workers.html",
                  {"workers": workers})
