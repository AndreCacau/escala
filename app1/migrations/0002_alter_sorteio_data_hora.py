# Generated by Django 3.2.7 on 2021-10-05 03:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sorteio',
            name='data_hora',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
