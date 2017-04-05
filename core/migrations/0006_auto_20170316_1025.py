# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20170316_0957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='ingredients',
            field=taggit.managers.TaggableManager(verbose_name='Ingredients', blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag'),
        ),
    ]
