# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0005_auto_20150122_0150'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='person',
            unique_together=set([('first_name', 'last_name', 'email')]),
        ),
    ]
