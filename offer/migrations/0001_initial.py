# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_restaurant_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='NumberCategoryOfferDiscount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('number', models.IntegerField()),
                ('category', models.ForeignKey(to='core.Category')),
            ],
        ),
        migrations.CreateModel(
            name='NumberCategoryOfferEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('number', models.IntegerField()),
                ('category', models.ForeignKey(to='core.Category')),
            ],
        ),
        migrations.CreateModel(
            name='NumberDishOfferDiscount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('number', models.IntegerField()),
                ('dish', models.ForeignKey(to='core.Dish')),
            ],
        ),
        migrations.CreateModel(
            name='NumberDishOfferEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('number', models.IntegerField()),
                ('dish', models.ForeignKey(to='core.Dish')),
            ],
        ),
        migrations.CreateModel(
            name='NumberMenuOfferDiscount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('number', models.IntegerField()),
                ('menu', models.ForeignKey(to='core.Menu')),
            ],
        ),
        migrations.CreateModel(
            name='NumberMenuOfferEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('number', models.IntegerField()),
                ('menu', models.ForeignKey(to='core.Menu')),
            ],
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=255)),
                ('nbrEntries', models.IntegerField()),
                ('nbrDiscount', models.IntegerField()),
                ('discount', models.IntegerField()),
                ('discountOnTotal', models.IntegerField()),
                ('discountCategories', models.ManyToManyField(related_name='discountOffers', to='core.Category', through='offer.NumberCategoryOfferDiscount')),
                ('discountDishes', models.ManyToManyField(related_name='discountOffers', to='core.Dish', through='offer.NumberDishOfferDiscount')),
                ('discountMenus', models.ManyToManyField(related_name='discountOffers', to='core.Menu', through='offer.NumberMenuOfferDiscount')),
                ('entryCategories', models.ManyToManyField(related_name='entryOffers', to='core.Category', through='offer.NumberCategoryOfferEntry')),
                ('entryDishes', models.ManyToManyField(related_name='entryOffers', to='core.Dish', through='offer.NumberDishOfferEntry')),
                ('entryMenus', models.ManyToManyField(related_name='entryOffers', to='core.Menu', through='offer.NumberMenuOfferEntry')),
                ('restaurant', models.ForeignKey(related_name='offers', to='core.Restaurant')),
            ],
        ),
        migrations.AddField(
            model_name='numbermenuofferentry',
            name='offer',
            field=models.ForeignKey(to='offer.Offer'),
        ),
        migrations.AddField(
            model_name='numbermenuofferdiscount',
            name='offer',
            field=models.ForeignKey(to='offer.Offer'),
        ),
        migrations.AddField(
            model_name='numberdishofferentry',
            name='offer',
            field=models.ForeignKey(to='offer.Offer'),
        ),
        migrations.AddField(
            model_name='numberdishofferdiscount',
            name='offer',
            field=models.ForeignKey(to='offer.Offer'),
        ),
        migrations.AddField(
            model_name='numbercategoryofferentry',
            name='offer',
            field=models.ForeignKey(to='offer.Offer'),
        ),
        migrations.AddField(
            model_name='numbercategoryofferdiscount',
            name='offer',
            field=models.ForeignKey(to='offer.Offer'),
        ),
    ]
