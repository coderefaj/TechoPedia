# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_jqcours_jscours_mycours'),
    ]

    operations = [
        migrations.AddField(
            model_name='gitcours',
            name='author',
            field=models.CharField(default=None, max_length=120),
        ),
        migrations.AddField(
            model_name='gitcours',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='gitcours',
            name='link',
            field=models.URLField(default=None, max_length=120),
        ),
        migrations.AddField(
            model_name='jqcours',
            name='author',
            field=models.CharField(default=None, max_length=120),
        ),
        migrations.AddField(
            model_name='jqcours',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='jqcours',
            name='link',
            field=models.URLField(default=None, max_length=120),
        ),
        migrations.AddField(
            model_name='jscours',
            name='author',
            field=models.CharField(default=None, max_length=120),
        ),
        migrations.AddField(
            model_name='jscours',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='jscours',
            name='link',
            field=models.URLField(default=None, max_length=120),
        ),
        migrations.AddField(
            model_name='linuxcours',
            name='author',
            field=models.CharField(default=None, max_length=120),
        ),
        migrations.AddField(
            model_name='linuxcours',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='linuxcours',
            name='link',
            field=models.URLField(default=None, max_length=120),
        ),
        migrations.AddField(
            model_name='mycours',
            name='author',
            field=models.CharField(default=None, max_length=120),
        ),
        migrations.AddField(
            model_name='mycours',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='mycours',
            name='link',
            field=models.URLField(default=None, max_length=120),
        ),
        migrations.AddField(
            model_name='pycours',
            name='author',
            field=models.CharField(default=None, max_length=120),
        ),
        migrations.AddField(
            model_name='pycours',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='pycours',
            name='link',
            field=models.URLField(default=None, max_length=120),
        ),
    ]
