# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-25 19:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('belt_exam', '0002_auto_20171125_1857'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='datehired',
            new_name='dob',
        ),
    ]
