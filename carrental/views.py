from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CarSerializer, CarReservationSerializer
from django.utils import timezone
import datetime
from carrental.services.carRentalService import CarRentalService

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
