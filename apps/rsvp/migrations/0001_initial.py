# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Rsvp',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('attendance', models.BooleanField()),
                ('guests', models.PositiveSmallIntegerField(default=0)),
                ('meal_preference', models.CharField(choices=[('CHI', 'Chicken'), ('VEG', 'Vegetarian')], max_length=3)),
                ('person', models.ForeignKey(to='rsvp.Person')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
