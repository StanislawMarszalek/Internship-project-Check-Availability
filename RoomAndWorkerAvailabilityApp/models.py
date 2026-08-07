"""
Models for the RoomAndWorkerAvailabilityApp
Models: Room, Worker, Reservvation
"""

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator
from django.utils.translation import gettext_lazy


class Room(models.Model):
    """
    Class to model the Room
    Attributes:
        room_number (int): Room number which is PK
        room_floor (int): Room floor
        room_name (str): Room name
        additional_room_info (str): Additional room info
        building_name (str): Name of building where the room is located
        creation_date (date): Date of creation
    """

    room_number = models.PositiveIntegerField(primary_key=True,default=1,
                                              verbose_name=gettext_lazy('Room number'))

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

    creation_date = models.DateField(auto_now_add=True,
                                     verbose_name=gettext_lazy('Date of creation'))

    class Meta:
        verbose_name = gettext_lazy('Room')
        verbose_name_plural = gettext_lazy('Rooms')

    def __str__(self):
        return (f"{gettext_lazy('Room number')}: {self.room_number}\n"
                f"{gettext_lazy('Floor')} {self.room_floor}"
                f"{f"\n Nazwa sali: {self.room_name}" if self.room_name else ""}")




class Worker(AbstractUser):

    """
    Class to model the Worker
    Attributes:
        username (string): Username
        first_name (string): First name
        last_name (string): Last name
        email (string): Email
        password (string): Password to login
        department (string): Department
        position (string): Position
        is_preset (boolean): Preset
        start_of_absence (date): Start of absence
        end_of_absence (date): Date of return
        reason_of_absence (string): Reason of absence
        creation_date (date): Date of creation
    """

    DEPARTMENTS = [
        ("IT", "IT"),
        ("HR", "HR"),
    ]

    POSITIONS = [
        ("Mayor", "Mayor"),
        ("Secretary", "Secretary"),
        ("Administrator", "Administrator"),
    ]
    department = models.CharField(
        max_length=25,
        choices=DEPARTMENTS
    )


    position = models.CharField(choices=POSITIONS,max_length=30, verbose_name=gettext_lazy('Position'))

    is_preset = models.BooleanField(default=True,verbose_name=gettext_lazy('Preset'))

    start_of_absence = models.DateField(null=True, blank=True,
                                        verbose_name=gettext_lazy('Start of the absence'))

    end_of_absence = models.DateField(null=True, blank=True)

    reason_of_absence = models.TextField(max_length=1500, blank=True,
                                         verbose_name=gettext_lazy('Reason of absence'))

    creation_date = models.DateField(auto_now_add=True,
                                     verbose_name=gettext_lazy('Date of creation'))

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

class Reservation(models.Model):
    """
    Class to model the Reservation
    Attributes:
        room (Room): Room id
        worker (Worker): Worker id
        start_of_reservation (date): Date of reservation
        end_of_reservation (date): Date of the end of reservation
        description_of_event (string): Description of the event
        pk (PrimaryKey): Primary key of the reservation
    """
    room = models.ForeignKey(Room, on_delete=models.CASCADE,
                             verbose_name=gettext_lazy('Room number'),related_name="reservations")

    worker = models.ForeignKey(Worker, on_delete=models.CASCADE,
                               verbose_name=gettext_lazy('Reserver id'),related_name="reservations")

    start_of_reservation = models.DateField(verbose_name=gettext_lazy('Start of the reservation'))

    end_of_reservation = models.DateField(verbose_name=gettext_lazy('End of the reservation'))

    description_of_event = models.TextField(max_length=1500, blank=True,null=True,
                                            verbose_name=gettext_lazy('Description of event'))

    pk = models.CompositePrimaryKey("worker", "room","start_of_reservation", "end_of_reservation")

    class Meta:
        verbose_name = gettext_lazy('Reservation')
        verbose_name_plural = gettext_lazy('Reservations')
