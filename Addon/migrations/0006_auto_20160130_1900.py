# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-30 19:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Addon', '0005_addon_sort_index'),
    ]

    operations = [
        migrations.RenameField(
            model_name='addon',
            old_name='discription_1',
            new_name='code_block',
        ),
        migrations.RenameField(
            model_name='addon',
            old_name='image_1_visibility',
            new_name='code_visibility',
        ),
        migrations.RenameField(
            model_name='addon',
            old_name='discription_2',
            new_name='discription',
        ),
        migrations.RenameField(
            model_name='addon',
            old_name='image_1',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='addon',
            old_name='image_2_visibility',
            new_name='image_visibility',
        ),
        migrations.RemoveField(
            model_name='addon',
            name='discription_3',
        ),
        migrations.RemoveField(
            model_name='addon',
            name='discription_4',
        ),
        migrations.RemoveField(
            model_name='addon',
            name='image_2',
        ),
        migrations.RemoveField(
            model_name='addon',
            name='image_3',
        ),
        migrations.RemoveField(
            model_name='addon',
            name='image_3_visibility',
        ),
        migrations.RemoveField(
            model_name='addon',
            name='image_4',
        ),
        migrations.RemoveField(
            model_name='addon',
            name='image_4_visibility',
        ),
        migrations.AddField(
            model_name='addon',
            name='post_block',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='addon',
            name='pre_block',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='addon',
            name='type_of_code',
            field=models.CharField(choices=[('javascript', 'javascript'), ('markup', 'markup'), ('css', 'css'), ('php', 'php')], default='markup', max_length=20),
        ),
    ]