# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20170412_1522'),
    ]

    operations = [
        migrations.CreateModel(
            name='NumberDishMenu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('number', models.IntegerField()),
                ('dish', models.ForeignKey(to='core.Dish')),
            ],
        ),
        migrations.AddField(
            model_name='menu',
            name='description',
            field=models.TextField(default='Classique'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='note',
            field=models.IntegerField(default=5, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='numberdishmenu',
            name='menu',
            field=models.ForeignKey(to='core.Menu'),
        ),
        migrations.AddField(
            model_name='menu',
            name='dishes',
            field=models.ManyToManyField(to='core.Dish', through='core.NumberDishMenu'),
        ),
    ]
