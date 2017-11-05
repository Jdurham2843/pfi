# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-05 05:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('type', models.CharField(choices=[('Debit', 'DB'), ('Credit', 'CR')], max_length=2)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.CharField(max_length=400)),
            ],
            options={
                'ordering': ('name', 'type', 'price', 'description'),
            },
        ),
    ]
