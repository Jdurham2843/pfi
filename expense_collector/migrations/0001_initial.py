# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-05 06:26
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('type', models.CharField(choices=[('DB', 'Debit'), ('CR', 'Credit')], max_length=2)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.CharField(max_length=400)),
            ],
            options={
                'ordering': ('name', 'type', 'price', 'description'),
            },
        ),
    ]
