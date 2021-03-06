# Generated by Django 2.2.4 on 2020-12-21 09:35

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0025_auto_20201220_1713'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='links',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.URLField(), blank=True, null=True, size=None),
        ),
        migrations.AddField(
            model_name='historicaldevice',
            name='links',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.URLField(), blank=True, null=True, size=None),
        ),
    ]
