from django.db import models
from djangoyearlessdate.models import YearField


class Car(models.Model):
    """
    Represents a car that can be rented
    """
    car_id = models.AutoField(primary_key=True)
    vendor = models.CharField(max_length=50)
    model = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    year = YearField()
    color = models.CharField(max_length=20)
    qty = models.IntegerField(default=0)
    avail = models.IntegerField(default=0)
    #TODO validate 0<=avail<=qty
    def __str__(self):
            return self.model

