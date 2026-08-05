"""
Models for the RoomAvailabilityApp
Models: Room
"""

from django.db import models
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
    room_number = models.PositiveIntegerField(default=1,verbose_name='Numer pokoju')

    room_floor = models.PositiveIntegerField(default=0,
                                             validators=[MaxValueValidator(2)],
                                             verbose_name='Piętro')

    room_name = models.CharField(max_length=150,blank=True,
                                 null=True,verbose_name='Nazwa pokoju')

    additional_room_info = models.TextField(max_length=3_000,blank=True,
                                            null=True,
                                            verbose_name='Dodatkowe informacje')

    building_name = models.CharField(max_length=1, blank=True,
                                     null=True, verbose_name='Nazwa budynku')

    creation_date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Room"
        verbose_name_plural = "Rooms"

    def __str__(self):
        return (f"Numer sali: {self.room_number}\nPiętro: {self.room_floor}"
                f"{"\n Nazwa sali: {self.room_name}" if self.room_name else ""}")
