# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_auto_20141102_0037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, through='courses.Subscription'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='resource',
            name='author',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='subscription',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='vote',
            name='voter',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
