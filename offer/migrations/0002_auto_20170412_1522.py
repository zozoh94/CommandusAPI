# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='numbercategoryofferdiscount',
            options={'verbose_name_plural': 'categories discounts'},
        ),
        migrations.AlterModelOptions(
            name='numbercategoryofferentry',
            options={'verbose_name_plural': 'categories entries'},
        ),
        migrations.AlterModelOptions(
            name='numberdishofferdiscount',
            options={'verbose_name_plural': 'dishes discounts'},
        ),
        migrations.AlterModelOptions(
            name='numberdishofferentry',
            options={'verbose_name_plural': 'dishes entries'},
        ),
        migrations.AlterModelOptions(
            name='numbermenuofferdiscount',
            options={'verbose_name_plural': 'menus discounts'},
        ),
        migrations.AlterModelOptions(
            name='numbermenuofferentry',
            options={'verbose_name_plural': 'menus entries'},
        ),
        migrations.AlterField(
            model_name='offer',
            name='discount',
            field=models.IntegerField(verbose_name='discount on the offer'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='discountOnTotal',
            field=models.IntegerField(verbose_name='discount on the total'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='nbrDiscount',
            field=models.IntegerField(verbose_name='maximum discount number'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='nbrEntries',
            field=models.IntegerField(verbose_name='minimum entries number'),
        ),
    ]
