# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_auto_20170501_1403'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('day', models.CharField(max_length=3, choices=[('MON', 'monday'), ('TUE', 'tuesday'), ('WED', 'wednesday'), ('THU', 'thursday'), ('FRI', 'friday'), ('SAT', 'saturday'), ('SUN', 'sunday')])),
                ('restaurant', models.ForeignKey(related_name='schedules', to='core.Restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='ScheduleTime',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('opening_time', models.TimeField()),
                ('closing_time', models.TimeField()),
                ('schedule', models.ForeignKey(related_name='times', to='core.Schedule')),
            ],
        ),
    ]
