# Generated by Django 2.2 on 2019-05-20 14:48

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0006_auto_20190515_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='description',
            field=tinymce.models.HTMLField(default='', verbose_name='Activity description'),
        ),
        migrations.AlterField(
            model_name='condition',
            name='description',
            field=tinymce.models.HTMLField(default='', verbose_name='Condition description'),
        ),
    ]