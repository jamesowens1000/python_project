# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-02-26 22:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meds', '0003_remove_dependent_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Age_group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('min_age', models.CharField(max_length=255)),
                ('max_age', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vaccinations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('abbreviation', models.CharField(max_length=255)),
                ('url', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='dependent',
            name='blood_type',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='dependent',
            name='height',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='dependent',
            name='weight',
            field=models.CharField(max_length=255, null=True),
        ),
    ]