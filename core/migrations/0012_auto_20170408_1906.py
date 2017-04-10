# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20170408_1401'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='NumberCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('number', models.IntegerField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.AlterModelOptions(
            name='dish',
            options={'verbose_name_plural': 'dishes'},
        ),
        migrations.AddField(
            model_name='numbercategory',
            name='category',
            field=models.ForeignKey(to='core.Category'),
        ),
        migrations.AddField(
            model_name='numbercategory',
            name='menu',
            field=models.ForeignKey(to='core.Menu'),
        ),
        migrations.AddField(
            model_name='menu',
            name='categories',
            field=models.ManyToManyField(to='core.Category', through='core.NumberCategory'),
        ),
        migrations.AddField(
            model_name='menu',
            name='restaurant',
            field=models.ForeignKey(related_name='menus', to='core.Restaurant'),
        ),
    ]
