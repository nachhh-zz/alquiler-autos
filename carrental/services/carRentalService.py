from carrental.models.Car import Car
from carrental.models.CarReservation import CarReservation
from django.db.models import Q
""" service utils for rental of cars
"""
class CarRentalService:
    """ get available cars in given range of dates
    """
    def getAvailCars(self, start, end):
       # first get all cars
       all_cars = Car.objects.all()
       # now get rented cars in given range
       rented_car_reservations = CarReservation.objects.filter(start_date__lte=start, end_date__gte=end)
       # extract the actual cars from the reservation list above for which vail=0
       rented_cars_not_avail = set([reservation.car for reservation in rented_car_reservations if reservation.car.avail==0])
       # finally get available cars by difference
       avail_cars = [car for car in all_cars if car not in rented_cars_not_avail]
       return avail_cars

    """ Get reservations in given range of dates
    """
    def getReservedCars(self, start, end):
        rented_car_reservations = CarReservation.objects.filter(Q( start_date__range=[start, end] ) | Q( end_date__range=[start, end]) )
        return rented_car_reservations
