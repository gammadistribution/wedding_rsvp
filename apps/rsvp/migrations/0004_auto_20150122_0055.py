# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0003_auto_20150119_2224'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='slug',
            field=models.SlugField(max_length=101, verbose_name='slug to identify person', default='matthew-tiger', editable=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.EmailField(verbose_name='email address submitted for person', max_length=254, serialize=False, primary_key=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='first_name',
            field=models.CharField(max_length=50, verbose_name='first name of person'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='last_name',
            field=models.CharField(max_length=50, verbose_name='last name of person'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rsvp',
            name='attendance',
            field=models.BooleanField(verbose_name='True if Person is attending', default=None),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rsvp',
            name='guests',
            field=models.PositiveSmallIntegerField(verbose_name='Number of guests of Person', default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rsvp',
            name='meal_preference',
            field=models.CharField(choices=[('CHI', 'Chicken'), ('VEG', 'Vegetarian')], max_length=3, verbose_name='Meal chosen by Person', default='CHI'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rsvp',
            name='person',
            field=models.OneToOneField(primary_key=True, serialize=False, verbose_name='Person associated to Rsvp', to='rsvp.Person'),
            preserve_default=True,
        ),
    ]
