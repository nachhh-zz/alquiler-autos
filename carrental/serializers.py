from rest_framework import serializers
from models.Car import Car

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('model', 'year', 'color', 'qty')
