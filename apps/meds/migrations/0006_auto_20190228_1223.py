# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-02-28 18:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meds', '0005_auto_20190227_1541'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Vaccinations',
            new_name='Vaccination',
        ),
        migrations.AddField(
            model_name='age_group',
            name='vaccinations',
            field=models.ManyToManyField(related_name='age_groups', to='meds.Vaccination'),
        ),
    ]
