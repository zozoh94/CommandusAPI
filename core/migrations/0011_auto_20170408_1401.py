# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20170326_1728'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=255)),
                ('restaurant', models.ForeignKey(related_name='categories', to='core.Restaurant')),
            ],
        ),
        migrations.AddField(
            model_name='dish',
            name='categories',
            field=models.ManyToManyField(related_name='dishes', to='core.Category'),
        ),
    ]
