# Generated by Django 2.2.3 on 2019-08-22 09:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0020_auto_20190822_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participation',
            name='fee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.Fee'),
        ),
    ]
