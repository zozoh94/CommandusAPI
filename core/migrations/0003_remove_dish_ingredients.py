# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-16 09:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_dish_notes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dish',
            name='ingredients',
        ),
    ]
