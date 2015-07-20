from django.db import models
from Car import Car
class CarReservation(models.Model):
    """
    Represents a rreservation of a car
    """ 
    car = models.ForeignKey(Car)
    start_date = models.DateTimeField('reservation start date')
    end_date = models.DateTimeField('reservation end date')
    def __str__(self):
        return "Reserve for %s from %s to %s" % (self.car.model, self.start_date, self.end_date)
