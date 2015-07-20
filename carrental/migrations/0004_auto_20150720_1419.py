# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import carrental.models.CarReservation


class Migration(migrations.Migration):

    dependencies = [
        ('carrental', '0003_car_avail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carreservation',
            name='end_date',
            field=models.DateTimeField(verbose_name=b'reservation end date', validators=[carrental.models.CarReservation.validate_dates_range]),
        ),
        migrations.AlterField(
            model_name='carreservation',
            name='start_date',
            field=models.DateTimeField(verbose_name=b'reservation start date', validators=[carrental.models.CarReservation.validate_dates_range]),
        ),
    ]
