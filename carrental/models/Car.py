from django.db import models
from djangoyearlessdate.models import YearField


class Car(models.Model):
    """
    Represents a car that can be rented
    """
    # TIM NOTE: models.Model subclass takes care of adding an auto-incremental
    # primary key id field so we don't need to.
    # https://docs.djangoproject.com/en/1.8/topics/db/models/#automatic-primary-key-fields
    car_id = models.AutoField(primary_key=True)
    vendor = models.CharField(max_length=50)
    model = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    year = YearField()
    color = models.CharField(max_length=20)
    qty = models.IntegerField(default=0)

    # TIM NOTE: This field is being used incorrectly. Every time a reservation for
    # a date range is made, this field is decreased by one, but in reality, I am
    # only decreasing by one for available cars *inside* of a given date range.
    # So, I can have 5 cars, and have 20 different reservations occuring on completely
    # different dates. According to your use of the field, this scenario would give me -15 availability,
    # which isn't possible.
    avail = models.IntegerField(default=0)
    # TODO validate 0<=avail<=qty

    def __str__(self):
        # Spacing should be only 4 spaces, not 8.
        return self.model
