# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-30 02:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='adorable_kittens',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('breed', models.CharField(max_length=150)),
                ('cat_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='humans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('human_name', models.CharField(max_length=150)),
                ('cat_overlord', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cats.adorable_kittens')),
            ],
        ),
    ]