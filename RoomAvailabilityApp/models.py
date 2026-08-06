"""
Models for the RoomAvailabilityApp
Models: Room
"""

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator
from django.utils.translation import gettext_lazy


class Room(models.Model):
    """
    Class to model the Room
    Attributes:
        pk: Primary Key made from "room_number" and "room_floor" atrributes
        room_number (int): Room number
        room_floor (int): Room floor
        room_name (str): Room name
        additional_room_info (str): Additional room info
        building_name (str): Name of building where the room is located
        creation_date (date): Date of creation
    """
    pk = models.CompositePrimaryKey("room_number", "room_floor")
    room_number = models.PositiveIntegerField(default=1,verbose_name=gettext_lazy('Room number'))

    room_floor = models.PositiveIntegerField(default=0,
                                             validators=[MaxValueValidator(2)],
                                             verbose_name=gettext_lazy('Floor'))

    room_name = models.CharField(max_length=150,blank=True,
                                 null=True,verbose_name=gettext_lazy('Room name'))

    additional_room_info = models.TextField(max_length=3_000,blank=True,
                                            null=True,
                                            verbose_name=gettext_lazy('Additional info'))

    building_name = models.CharField(max_length=1, blank=True,
                                     null=True, verbose_name=gettext_lazy('Building name'))

    creation_date = models.DateField(auto_now_add=True,verbose_name=gettext_lazy('Date of creation'))

    class Meta:
        verbose_name = gettext_lazy('Room')
        verbose_name_plural = gettext_lazy('Rooms')

    def __str__(self):
        return (f"{gettext_lazy('Room number')}: {self.room_number}\n"
                f"{gettext_lazy('Floor')} {self.room_floor}"
                f"{f"\n Nazwa sali: {self.room_name}" if self.room_name else ""}")




class Worker(AbstractUser):

    DEPARTMENTS = [
        ("IT", "IT"),
        ("HR", "HR"),
    ]

    department = models.CharField(
        max_length=10,
        choices=DEPARTMENTS
    )

    position = models.CharField(max_length=30)

    is_preset = models.BooleanField(default=False)

    start_of_absence = models.DateField(null=True, blank=True)
    end_of_absence = models.DateField(null=True, blank=True)
    reason_of_absence = models.TextField(max_length=1500, blank=True)

    creation_date = models.DateField(auto_now_add=True)

    REQUIRED_FIELDS = [
        "first_name",
        "last_name",
        "email",
        "department",
        "position",
    ]

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["first_name", "last_name", "department"],
                name="unique_worker"
            )
        ]
