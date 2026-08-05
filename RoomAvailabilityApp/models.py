from django.db import models
from django.core.validators import MaxValueValidator

class Room(models.Model):
    pk = models.CompositePrimaryKey("room_number", "room_floor")
    room_number = models.PositiveIntegerField(default=1,verbose_name='Numer pokoju')
    room_floor = models.PositiveIntegerField(default=0,validators=[MaxValueValidator(2)],verbose_name='Piętro')
    room_name = models.CharField(max_length=150,blank=True,null=True,verbose_name='Nazwa pokoju')
    building_name = models.CharField(max_length=1,blank=True,null=True,verbose_name='Nazwa budynku')
    additional_room_info = models.TextField(max_length=3_000,blank=True,null=True,verbose_name='Dodatkowe informacje')

    creation_date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Sala"
        verbose_name_plural = "Sale"

    def __str__(self):
        return (f"Numer sali: {self.room_number}\nPiętro: {self.room_floor}"
                f"{"\n Nazwa sali: {self.room_name}" if self.room_name else ""}")

