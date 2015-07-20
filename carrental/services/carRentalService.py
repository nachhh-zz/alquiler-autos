from carrental.models.Car import Car
from carrental.models.CarReservation import CarReservation
""" service utils for rental of cars
"""
class CarRentalService:
    """
    get available cars in given range of dates
    """
    def getAvailCars(self, start, end):
       # first get all cars
       all_cars = Car.objects.all()
       # now get rented cars in given range
       rented_car_reservations = CarReservation.objects.filter(start_date__lte=start, end_date__gte=end)
       all_rented_cars = CarReservation.objects.all()
       # extract the actual cars from the reservation list above
       rented_cars = set([reservation.car for reservation in rented_car_reservations])
       # finally get available cars by difference
       avail_cars = [car for car in all_cars if car not in rented_cars]
       return avail_cars
