# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-27 17:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('semacomp2016', '0004_sponsor_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsor',
            name='image',
            field=models.ImageField(upload_to='semacomp2016/static/img/sponsor/'),
        ),
    ]
