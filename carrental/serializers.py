from rest_framework import serializers
from models.Car import Car
from models.CarReservation import CarReservation

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('model', 'year', 'color', 'qty', 'avail')

class CarReservationSerializer(serializers.ModelSerializer):
    car = CarSerializer()
    class Meta:
        model = CarReservation
        fields = ('car', 'start_date', 'end_date')
