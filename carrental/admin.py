from django.contrib import admin
from .models.Car import Car
from .models.CarReservation import CarReservation

class ReservationInline(admin.StackedInline):
    model = CarReservation
    extra = 1
class CarAdmin(admin.ModelAdmin):
    inlines = [ReservationInline]
    list_display = ('model', 'vendor', 'description', 'year', 'color', 'qty', 'avail')
    search_fields = ['vendor', 'model', 'description', 'year']
    list_filter = ['year', 'vendor']    
#TODO add a way to limit dates available in calendar taking into account
# the already reserved ranges and the avail of a given car (??)
admin.site.register(Car, CarAdmin)
admin.site.register(CarReservation)

