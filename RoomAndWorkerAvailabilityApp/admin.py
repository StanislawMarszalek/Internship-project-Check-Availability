
from django.contrib import admin
from .models import Room, Worker

# Register your models here.

from django.contrib import admin, messages
from django.shortcuts import redirect

from .models import Room, Worker


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):

    def response_add(self, request, obj, post_url_continue=None):
        messages.success(
            request,
            f"Room {obj.room_number} was successfully added."
        )

        if "_continue" in request.POST:
            return redirect(
                "admin:RoomAndWorkerAvailabilityApp_room_change",
                obj.pk
            )

        if "_addanother" in request.POST:
            return redirect(
                "admin:RoomAndWorkerAvailabilityApp_room_add"
            )

        return redirect("availability:rooms_list")

    def response_change(self, request, obj):
        messages.success(
            request,
            f"Room {obj.room_number} was successfully updated."
        )

        if "_continue" in request.POST:
            return redirect(
                "admin:RoomAndWorkerAvailabilityApp_room_change",
                obj.pk
            )
        if "_addanother" in request.POST:
            return redirect(
                "admin:RoomAndWorkerAvailabilityApp_room_add"
            )

        return redirect("availability:rooms_list")

    def response_delete(self, request, obj_display, obj_id):
        messages.success(
            request,
            f"Room {obj_display} was successfully deleted."
        )

        return redirect("availability:rooms_list")

@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):

    def response_add(self, request, obj, post_url_continue=None):
        messages.success(
            request,
            f"Worker {obj.first_name} {obj.last_name} was successfully added."
        )

        if "_continue" in request.POST:
            return redirect(
                "admin:RoomAndWorkerAvailabilityApp_worker_change",
                obj.pk
            )

        if "_addanother" in request.POST:
            return redirect(
                "admin:RoomAndWorkerAvailabilityApp_worker_add"
            )

        return redirect("availability:workers_list")

    def response_change(self, request, obj):
        messages.success(
            request,
            f"Worker {obj.first_name} {obj.last_name} was successfully updated."
        )

        if "_continue" in request.POST:
            return redirect(
                "admin:RoomAndWorkerAvailabilityApp_worker_change",
                obj.pk
            )

        if "_addanother" in request.POST:
            return redirect(
                "admin:RoomAndWorkerAvailabilityApp_worker_add"
            )

        return redirect("availability:workers_list")

    def response_delete(self, request, obj_display, obj_id):
        messages.success(
            request,
            f"Worker {obj_display} was successfully deleted."
        )

        return redirect("availability:workers_list")