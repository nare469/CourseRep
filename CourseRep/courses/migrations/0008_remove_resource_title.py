# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_auto_20141102_0337'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resource',
            name='title',
        ),
    ]
