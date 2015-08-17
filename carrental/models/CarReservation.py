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
    Represents a reservation of a car
    """
    # TIM NOTE: The related name here is the name a Car instance would use to get its
    # related reservations, so it makes more sense here to use the word "reservations", not "car".
    # In this way, you would be accessing the reservations like this:
    #   car = Car.objects.get(id=car_id)
    #   reservations = car.reservations.all()
    car = models.ForeignKey(Car, related_name='reservations')
    start_date = models.DateTimeField('reservation start date', validators=[validate_dates_range])
    end_date = models.DateTimeField('reservation end date', validators=[validate_dates_range])

    def __str__(self):
        return u"Reservation for %s from %s to %s" % (self.car.model, self.start_date, self.end_date)

    # Missing 'self' as first arguement.
    def validate_dates_range(self, value):
        if value < timezone.now():
            raise ValidationError('%s is not a valid date!' % value)
