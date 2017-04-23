# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20170415_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
