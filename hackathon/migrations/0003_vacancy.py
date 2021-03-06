# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-07-27 15:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackathon', '0002_profession'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, max_length=255, null=True)),
                ('region_code', models.CharField(blank=True, max_length=255, null=True)),
                ('region_name', models.CharField(blank=True, max_length=255, null=True)),
                ('salary_min', models.CharField(blank=True, max_length=255, null=True)),
                ('salary_max', models.CharField(blank=True, max_length=255, null=True)),
                ('job_name', models.CharField(blank=True, max_length=255, null=True)),
                ('duty', models.CharField(blank=True, max_length=255, null=True)),
                ('education', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
