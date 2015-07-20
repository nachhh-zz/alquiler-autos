# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carrental', '0002_car_vendor'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='avail',
            field=models.IntegerField(default=0),
        ),
    ]
