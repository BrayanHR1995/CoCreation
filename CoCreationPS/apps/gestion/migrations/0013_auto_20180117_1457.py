# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-17 19:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0012_auto_20180117_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portafoliops',
            name='ruta_imagen',
            field=models.ImageField(upload_to='portafoliops/'),
        ),
    ]
