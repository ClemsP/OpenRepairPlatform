# Generated by Django 2.2 on 2019-05-21 15:14

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0006_merge_20190521_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalplace',
            name='description',
            field=tinymce.models.HTMLField(default='', verbose_name='Place description'),
        ),
    ]
