# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-18 20:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0007_entrada_vuelto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entrada',
            name='vuelto',
        ),
    ]