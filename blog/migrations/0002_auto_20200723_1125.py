# Generated by Django 3.0.5 on 2020-07-23 05:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mlproject',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 7, 23, 11, 25, 48, 642292)),
        ),
        migrations.AlterField(
            model_name='pythonproject',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 7, 23, 11, 25, 48, 641291)),
        ),
        migrations.AlterField(
            model_name='webdevproject',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 7, 23, 11, 25, 48, 642292)),
        ),
    ]