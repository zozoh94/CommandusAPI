# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_auto_20170501_2154'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, blank=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='address',
            field=models.CharField(max_length=255, blank=True, default=''),
            preserve_default=False,
        ),
    ]
