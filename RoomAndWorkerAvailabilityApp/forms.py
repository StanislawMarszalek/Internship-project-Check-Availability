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

class ChangeStatusForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields=["start_of_absence","end_of_absence","reason_of_absence"]

        widgets = {
            "start_of_absence":forms.DateInput(attrs={"class": "form-control","type":"date"}),
            "end_of_absence":forms.DateInput(attrs={"class": "form-control","type":"date"}),
            "reason_of_absence":forms.TextInput(attrs={"class": "form-control"}),
        }

    def clean(self):
        cleaned_data = super().clean()

        start = cleaned_data.get("start_of_absence")
        end = cleaned_data.get("end_of_absence")
        reason = cleaned_data.get("reason_of_absence")

        if not start:
            self.add_error(
                "start_of_absence",
                "Start date of absence is required."
            )

        if not end:
            self.add_error(
                "end_of_absence",
                "End date of absence is required."
            )

        if not reason or not reason.strip():
            self.add_error(
                "reason_of_absence",
                "Reason for absence is required."
            )

        if start and end and start > end:
            self.add_error(
                "end_of_absence",
                "End date cannot be earlier than start date."
            )

        return cleaned_data