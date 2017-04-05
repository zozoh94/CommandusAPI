# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20170323_1117'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='restaurant',
            field=models.ForeignKey(default=1, related_name='dishes', to='core.Restaurant'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='lat',
            field=models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=8),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='lon',
            field=models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=8),
        ),
    ]
