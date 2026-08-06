from django import forms
from RoomAndWorkerAvailabilityApp.models import Room, Worker
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class AddWorkerForm(UserCreationForm):
    class Meta:
        model = Worker
        fields = ["username","first_name", "last_name" ,"email", "password1", "password2","department","position"]
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "password1": forms.PasswordInput(attrs={"class": "form-control"}),
            "password2": forms.PasswordInput(attrs={"class": "form-control"}),
            "department": forms.Select(attrs={"class": "form-control"}),
            "position": forms.Select(attrs={"class": "form-control"}),
        }