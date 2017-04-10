# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20170408_2039'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='restaurant_picture'),
        ),
    ]
