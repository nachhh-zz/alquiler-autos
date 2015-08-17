from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone

from Car import Car


# validate dates range
def validate_dates_range(value):
    if value < timezone.now():
        raise ValidationError('%s is not a valid date!' % value)
class CarReservation(models.Model):
    """
    Represents a rreservation of a car
    """
    def validate_dates_range(value):
        if value < timezone.now():
            raise ValidationError('%s is not a valid date!' % value)
    car = models.ForeignKey(Car, related_name='car')
    start_date = models.DateTimeField('reservation start date', validators=[validate_dates_range])
    end_date = models.DateTimeField('reservation end date', validators=[validate_dates_range])
    #def clean(self):
    def __str__(self):
        return "Reserve for %s from %s to %s" % (self.car.model, self.start_date, self.end_date)
