
from django.contrib import admin
from schedule.models import Rule

from .models import Room, Worker

# Register your models here.

from django.contrib import admin, messages
from django.shortcuts import redirect

from .models import Room, Worker
from schedule.admin import RuleAdmin as SchedulerRuleAdmin

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):

    def response_add(self, request, obj, post_url_continue=None):
        messages.success(
            request,
            f"Room {obj.id} was successfully added."
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
            f"Room {obj.id} was successfully updated."
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



admin.site.unregister(Rule)
@admin.register(Rule)
class RuleAdmin(SchedulerRuleAdmin):

    def response_add(self, request, obj, post_url_continue=None):
        messages.success(
            request,
            f"Rule {obj.name} was successfully added."
        )

        if "_continue" in request.POST:
            return redirect(
                "admin:schedule_rule_change",
                obj.pk
            )

        if "_addanother" in request.POST:
            return redirect(
                "admin:schedule_rule_add"
            )

        return redirect(
            "availability:rules_list"
        )

    def response_change(self, request, obj):
        messages.success(
            request,
            f"Rule {obj.name} was successfully updated."
        )

        if "_continue" in request.POST:
            return redirect(
                "admin:schedule_rule_change",
                obj.pk
            )

        if "_addanother" in request.POST:
            return redirect(
                "admin:schedule_rule_add"
            )

        return redirect(
            "availability:rules_list"
        )

    def response_delete(self, request, obj_display, obj_id):
        messages.success(
            request,
            f"Rule {obj_display} was successfully deleted."
        )

        return redirect(
            "availability:rules_list"
        )