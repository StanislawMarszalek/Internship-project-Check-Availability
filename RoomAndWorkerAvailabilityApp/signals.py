from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from schedule.models import Calendar

from .models import Room


@receiver(post_save, sender=Room)
def create_room_calendar(sender, instance, created, **kwargs):
    """Function to create the Room Calendar after receiving post_save signal"""
    if created:
        Calendar.objects.get_or_create_calendar_for_object(
            instance,
            name=f"Room {instance.id}",
        )


@receiver(post_delete, sender=Room)
def delete_room_calendar(sender, instance, **kwargs):
    """Function to delete the Room Calendar after receiving post_delete signal"""
    calendars = Calendar.objects.get_calendars_for_object(instance)

    for calendar in calendars:
        calendar.delete()