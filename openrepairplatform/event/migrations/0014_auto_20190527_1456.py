# Generated by Django 2.2 on 2019-05-27 12:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0013_auto_20190527_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participation',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participations', to='event.Event'),
        ),
    ]
