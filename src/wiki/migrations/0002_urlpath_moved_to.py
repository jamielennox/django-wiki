# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-06 23:18
from __future__ import unicode_literals

import django.db.models.deletion
import mptt.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='urlpath',
            name='moved_to',
            field=mptt.fields.TreeForeignKey(blank=True, help_text='Article path was moved to this location', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='moved_from', to='wiki.URLPath', verbose_name='Moved to'),
        ),
    ]
