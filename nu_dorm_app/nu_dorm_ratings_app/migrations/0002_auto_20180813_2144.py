# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-14 02:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nu_dorm_ratings_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dorm',
            name='picture',
            field=models.ImageField(null=True, upload_to=b''),
        ),
    ]
