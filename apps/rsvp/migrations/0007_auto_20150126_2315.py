# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0006_auto_20150122_2356'),
    ]

    operations = [
        migrations.AddField(
            model_name='rsvp',
            name='music_preference',
            field=models.CharField(max_length=500, null=True, verbose_name='Music chosen by person'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rsvp',
            name='meal_preference',
            field=models.CharField(max_length=3, choices=[('CHI', 'Chicken'), ('VEG', 'Vegetarian')], null=True, verbose_name='Meal chosen by Person'),
            preserve_default=True,
        ),
    ]
