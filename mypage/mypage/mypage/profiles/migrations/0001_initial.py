# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='course_name',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128)),
                ('content', models.TextField(default='Welcome to the course')),
                ('url', models.CharField(max_length=128)),
                ('img_url', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField(default='description default text')),
                ('location', models.CharField(default='my location', max_length=128, null=True, blank=True)),
                ('job', models.CharField(max_length=128, null=True)),
            ],
        ),
    ]
