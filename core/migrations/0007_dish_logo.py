# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20170316_1025'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='dish_picture'),
        ),
    ]
