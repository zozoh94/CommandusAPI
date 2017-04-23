# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_auto_20170415_1643'),
        ('offer', '0003_offer_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='offer',
            old_name='discountOnTotal',
            new_name='discount_on_total',
        ),
        migrations.RenameField(
            model_name='offer',
            old_name='nbrDiscount',
            new_name='nbr_discount',
        ),
        migrations.RenameField(
            model_name='offer',
            old_name='nbrEntries',
            new_name='nbr_entries',
        ),
        migrations.RemoveField(
            model_name='offer',
            name='discountCategories',
        ),
        migrations.RemoveField(
            model_name='offer',
            name='discountDishes',
        ),
        migrations.RemoveField(
            model_name='offer',
            name='discountMenus',
        ),
        migrations.RemoveField(
            model_name='offer',
            name='entryCategories',
        ),
        migrations.RemoveField(
            model_name='offer',
            name='entryDishes',
        ),
        migrations.RemoveField(
            model_name='offer',
            name='entryMenus',
        ),
        migrations.AddField(
            model_name='offer',
            name='discount_categories',
            field=models.ManyToManyField(related_name='discount_offers', to='core.Category', through='offer.NumberCategoryOfferDiscount'),
        ),
        migrations.AddField(
            model_name='offer',
            name='discount_dishes',
            field=models.ManyToManyField(related_name='discount_offers', to='core.Dish', through='offer.NumberDishOfferDiscount'),
        ),
        migrations.AddField(
            model_name='offer',
            name='discount_menus',
            field=models.ManyToManyField(related_name='discount_offers', to='core.Menu', through='offer.NumberMenuOfferDiscount'),
        ),
        migrations.AddField(
            model_name='offer',
            name='entry_categories',
            field=models.ManyToManyField(related_name='entry_offers', to='core.Category', through='offer.NumberCategoryOfferEntry'),
        ),
        migrations.AddField(
            model_name='offer',
            name='entry_dishes',
            field=models.ManyToManyField(related_name='entry_offers', to='core.Dish', through='offer.NumberDishOfferEntry'),
        ),
        migrations.AddField(
            model_name='offer',
            name='entry_menus',
            field=models.ManyToManyField(related_name='entry_offers', to='core.Menu', through='offer.NumberMenuOfferEntry'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
