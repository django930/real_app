# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-14 12:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0002_auto_20190313_1002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertydetails',
            name='property_img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
