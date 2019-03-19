# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-18 13:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0006_auto_20190316_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertydetails',
            name='property_doc',
            field=models.FileField(blank=True, null=True, upload_to='document/'),
        ),
        migrations.AlterField(
            model_name='propertydetails',
            name='property_img',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
