import datetime

from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import CarSerializer, CarReservationSerializer
from carrental.services.carRentalService import CarRentalService


@api_view(['GET'])
def available_cars(request, car_id=None, start=None, end=None):
    """
    List all cars or available cars in given range or cars for which avail > 0
    (that is, models for which there are available car instances)
    """
    service = CarRentalService()
    cars = service.getAvailCars(car_id=car_id, start=start, end=end)
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


# TIM NOTE: Since we are creating objects here, we should be using POST, not GET.
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
            # TIM NOTE: According to REST, since the reservation was not saved successfully,
            # we need to return a non-200 Response to the client, probably some sort of 400...
            # http://codeplanet.io/principles-good-restful-api-design/
            # Search "Status Codes"
            # Also: All response bodies should contain JSON.
            return Response({'The car requested is unavailable'})
        serializer = CarReservationSerializer(carReservation, many=False)
        return Response(serializer.data)

    except ObjectDoesNotExist:
        # TIM NOTE: Same thing as mentioned above.
        return Response({'The car requested does not exist'})
