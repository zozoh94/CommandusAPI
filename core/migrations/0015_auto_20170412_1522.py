# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_restaurant_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
            ],
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='lat',
            field=models.DecimalField(verbose_name='latitude', blank=True, null=True, max_digits=10, decimal_places=8),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='lon',
            field=models.DecimalField(verbose_name='longitude', blank=True, null=True, max_digits=10, decimal_places=8),
        ),
        migrations.AddField(
            model_name='review',
            name='restaurant',
            field=models.ForeignKey(related_name='reviews', to='core.Restaurant'),
        ),
    ]
