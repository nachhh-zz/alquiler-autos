from carrental.models.Car import Car
from carrental.models.CarReservation import CarReservation
from django.db.models import Q
import datetime
""" service utils for rental of cars
"""
class CarRentalService:
    """ get available cars in giiven range of dates
    """
    def getAvailCars(self, car_id, start, end):
       if(car_id is None):
           if(start is None or end is None):
                #just check if avail > 0
                return Car.objects.filter(avail__gt=0)
           # first get all cars
           all_cars = Car.objects.all()
           # now get rented cars in given range
           rented_car_reservations = CarReservation.objects.filter( Q( start_date__range=[start, end] ) | Q( end_date__range=[start, end]) )
       else:
            if(start is None or end is None):
                #just check if avail > 0
                return Car.objects.filter(pk=car_id,avail__gt=0)
            # first get all cars with pk=car_id
            all_cars = Car.objects.filter(pk=car_id)
            # now get rented cars in given range
            rented_car_reservations = CarReservation.objects.filter(car__car_id=car_id).filter( Q( start_date__range=[start, end] ) | Q( end_date__range=[start, end]) )
       # extract the actual cars from the reservation list above for which avail=0
       rented_cars_not_avail = set([reservation.car for reservation in rented_car_reservations if reservation.car.avail==0])
       # finally get available cars by difference
       avail_cars = [car for car in all_cars if car not in rented_cars_not_avail]
       return avail_cars

    """ Get reservations in given range of dates
    """
    def getReservedCars(self, start, end):
        rented_car_reservations = CarReservation.objects.filter(Q( start_date__range=[start, end] ) | Q( end_date__range=[start, end]) )
        return rented_car_reservations
    """Make a car reservation given a car_id, start and end dates only if
        given car is available or if given range does not overlap with existing resevations
        for that car
    """
    def makeReservation(self, car_id, start, end):
        # check that there is car availability for the given range
        # or the given range does not overlap with other reservations
        requested_car = Car.objects.get(pk=car_id)
        print(requested_car.model)
        if requested_car is None:
            raise ValueError('the %i id is not valid' % car_id)
        reservation = CarReservation()
        # check if dates overlap with existing reservations when there is no avail
        other_reservations_overlapping = CarReservation.objects.filter(car=car_id). \
        filter(Q( start_date__range=[start, end] ) | Q( end_date__range=[start, end]))
        if other_reservations_overlapping and requested_car.avail == 0:
            return None
        #%z is supported in Python 3.2+ but not in 2.7, so hardcoding +00:00
        reservation.start_date = datetime.datetime.strptime(start,"%Y-%m-%d %H:%M:%S+00:00")
        reservation.end_date = datetime.datetime.strptime(end,"%Y-%m-%d %H:%M:%S+00:00")
        reservation.car = requested_car
        reservation.save()
        requested_car.avail -= 1
        requested_car.save()
        return reservation
