# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0004_auto_20150122_0055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rsvp',
            name='meal_preference',
            field=models.CharField(verbose_name='Meal chosen by Person', max_length=3, null=True, choices=[('CHI', 'Chicken'), ('VEG', 'Vegetarian')], default='CHI'),
            preserve_default=True,
        ),
    ]
