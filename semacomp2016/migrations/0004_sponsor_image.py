# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-25 17:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('semacomp2016', '0003_auto_20160725_1718'),
    ]

    operations = [
        migrations.AddField(
            model_name='sponsor',
            name='image',
            field=models.ImageField(default='sponsor/Unifesp.jpg', upload_to='sponsor/'),
        ),
    ]
