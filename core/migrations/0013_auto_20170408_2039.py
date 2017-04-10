# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20170408_1906'),
    ]

    operations = [
        migrations.CreateModel(
            name='NumberCategoryMenu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('number', models.IntegerField()),
                ('category', models.ForeignKey(to='core.Category')),
            ],
        ),
        migrations.RemoveField(
            model_name='numbercategory',
            name='category',
        ),
        migrations.RemoveField(
            model_name='numbercategory',
            name='menu',
        ),
        migrations.AlterField(
            model_name='menu',
            name='categories',
            field=models.ManyToManyField(to='core.Category', through='core.NumberCategoryMenu'),
        ),
        migrations.DeleteModel(
            name='NumberCategory',
        ),
        migrations.AddField(
            model_name='numbercategorymenu',
            name='menu',
            field=models.ForeignKey(to='core.Menu'),
        ),
    ]
