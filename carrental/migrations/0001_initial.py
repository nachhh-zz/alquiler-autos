# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import djangoyearlessdate.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('car_id', models.AutoField(serialize=False, primary_key=True)),
                ('model', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('year', djangoyearlessdate.models.YearField()),
                ('color', models.CharField(max_length=20)),
                ('qty', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='CarReservation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_date', models.DateTimeField(verbose_name=b'reservation start date')),
                ('end_date', models.DateTimeField(verbose_name=b'reservation end date')),
                ('car', models.ForeignKey(to='carrental.Car')),
            ],
        ),
    ]
