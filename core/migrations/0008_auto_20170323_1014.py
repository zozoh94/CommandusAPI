# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_dish_logo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dish',
            old_name='logo',
            new_name='picture',
        ),
    ]
