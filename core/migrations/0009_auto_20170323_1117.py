# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20170323_1014'),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255, null=True)),
                ('lat', models.DecimalField(null=True, max_digits=10, decimal_places=8)),
                ('lon', models.DecimalField(null=True, max_digits=10, decimal_places=8)),
            ],
        ),
        migrations.AlterField(
            model_name='dish',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
