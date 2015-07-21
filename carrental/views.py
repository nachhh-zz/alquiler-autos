from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CarSerializer, CarReservationSerializer
from django.utils import timezone
import datetime
from carrental.services.carRentalService import CarRentalService
from django.core.exceptions import ObjectDoesNotExist
@api_view(['GET'])
def available_cars(request, start=timezone.now(), end=timezone.now() + datetime.timedelta(days=365)):
    """
    List all cars or available cars in given range (by default show available cars in the year)
    """
    service = CarRentalService()
    cars = service.getAvailCars(start=start, end=end)
    serializer = CarSerializer(cars, many=True)
    return Response(serializer.data)
  
@api_view(['GET'])
def reserved_cars(request, start=timezone.now(), end=timezone.now() + datetime.timedelta(days=365)):
    """
    List all cars or available cars in given range (by default show available cars in the year)
    """
    service = CarRentalService()
    reservations = service.getReservedCars(start=start, end=end)
    serializer = CarReservationSerializer(reservations, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def rent_car(request, car_id, start=timezone.now(), end=timezone.now() + datetime.timedelta(days=1)):
    """
    Make a reservation of a car by id (by default rent for 1 day)
    """
    service = CarRentalService()
    try:
        carReservation = service.makeReservation(car_id=car_id, start=start, end=end)
        print(carReservation)
        if carReservation is None:
            return Response({'The car requested is unavailable'})
        serializer = CarReservationSerializer(carReservation, many=False)
        return Response(serializer.data)
    except ObjectDoesNotExist:
        return Response({'The car requested does not exist'})

