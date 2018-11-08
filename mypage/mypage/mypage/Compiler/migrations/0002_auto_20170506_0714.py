# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Compiler', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='compiler',
            old_name='program',
            new_name='txt',
        ),
    ]
