# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_auto_20170503_1846'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='delivery_time',
            field=models.DurationField(null=True),
        ),
    ]
