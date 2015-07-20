from django.contrib import admin
from .models.Car import Car
from .models.CarReservation import CarReservation

admin.site.register(Car)
admin.site.register(CarReservation)

