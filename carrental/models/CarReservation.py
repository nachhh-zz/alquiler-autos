from django.db import models
from Car import Car
class CarReservation(models.Model):
    """
    Represents a rreservation of a car
    """ 
    car = models.ForeignKey(Car)
    start_date = models.DateTimeField('reservation start date')
    end_date = models.DateTimeField('reservation end date')
