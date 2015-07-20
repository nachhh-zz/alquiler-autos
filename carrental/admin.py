from django.contrib import admin
from .models.Car import Car
from .models.CarReservation import CarReservation

class ReservationInline(admin.StackedInline):
    model = CarReservation
    extra = 1
class CarAdmin(admin.ModelAdmin):
    inlines = [ReservationInline]
    list_display = ('model', 'vendor', 'description', 'year', 'color', 'qty')
    search_fields = ['vendor', 'model', 'description', 'year']
    list_filter = ['year', 'vendor']    

admin.site.register(Car, CarAdmin)
admin.site.register(CarReservation)

