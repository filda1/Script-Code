# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-16 19:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_asesor',
            new_name='is_colaborador',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='is_coasesor',
            new_name='is_gerente',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_jurado',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_tesista',
        ),
    ]
