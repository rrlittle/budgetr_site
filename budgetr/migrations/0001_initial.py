# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-30 21:08
from __future__ import unicode_literals

from django.db import migrations, models
import recurrence.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('memo', models.CharField(blank=True, max_length=200, null=True)),
                ('amount', models.FloatField()),
                ('recurrence', recurrence.fields.RecurrenceField()),
            ],
        ),
    ]
