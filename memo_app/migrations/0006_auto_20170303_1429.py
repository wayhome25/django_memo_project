# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-03 05:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memo_app', '0005_auto_20170303_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memos',
            name='text',
            field=models.TextField(db_column='내용', help_text='메모 내용은 150자 이내로 입력 가능합니다.', max_length=180),
        ),
    ]