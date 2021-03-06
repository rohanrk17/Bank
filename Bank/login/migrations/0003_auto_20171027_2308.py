# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-27 17:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('desc', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Post'),
        ),
    ]
