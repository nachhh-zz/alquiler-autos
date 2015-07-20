# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carrental', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='vendor',
            field=models.CharField(default='Chevrolet', max_length=50),
            preserve_default=False,
        ),
    ]
