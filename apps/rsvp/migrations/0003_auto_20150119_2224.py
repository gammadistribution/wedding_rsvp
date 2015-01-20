# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0002_auto_20150119_2211'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='id',
        ),
        migrations.RemoveField(
            model_name='rsvp',
            name='id',
        ),
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.EmailField(serialize=False, primary_key=True, max_length=254),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rsvp',
            name='person',
            field=models.OneToOneField(serialize=False, primary_key=True, to='rsvp.Person'),
            preserve_default=True,
        ),
    ]
