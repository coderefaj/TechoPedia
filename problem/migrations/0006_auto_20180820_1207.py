# Generated by Django 2.0.7 on 2018-08-20 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problem', '0005_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testcase',
            name='input_case',
        ),
        migrations.RemoveField(
            model_name='testcase',
            name='output_case',
        ),
        migrations.AddField(
            model_name='testcase',
            name='input_file',
            field=models.FileField(default='none', upload_to='input/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='testcase',
            name='output_file',
            field=models.FileField(default='none', upload_to='output/'),
            preserve_default=False,
        ),
    ]
