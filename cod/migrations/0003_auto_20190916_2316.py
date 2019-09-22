# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-09-16 18:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cod', '0002_auto_20190902_2225'),
    ]

    operations = [
        migrations.AddField(
            model_name='cod',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Дата создания'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cod',
            name='tegs',
            field=models.ForeignKey(blank=True, db_column='tags', null=True, on_delete=django.db.models.deletion.CASCADE, to='cod.Tags'),
        ),
        migrations.AlterField(
            model_name='tags',
            name='name',
            field=models.CharField(default='', max_length=20, unique=True),
        ),
    ]
