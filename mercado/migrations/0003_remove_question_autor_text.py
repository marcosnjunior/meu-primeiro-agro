# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-18 11:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mercado', '0002_question_autor_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='autor_text',
        ),
    ]
