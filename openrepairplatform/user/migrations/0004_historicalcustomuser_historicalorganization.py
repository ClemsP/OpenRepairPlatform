# Generated by Django 2.2 on 2019-05-21 07:49

import openrepairplatform.utils
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_customuser_is_visible'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalOrganization',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100, verbose_name='Organization name')),
                ('description', models.TextField(default='', verbose_name='Activity description')),
                ('picture', models.TextField(max_length=100, validators=[openrepairplatform.utils.validate_image], verbose_name='Image')),
                ('slug', models.SlugField(default='')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical organization',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalCustomUser',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(db_index=True, max_length=254, verbose_name='email address')),
                ('first_name', models.CharField(default='', max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(default='', max_length=30, verbose_name='last name')),
                ('street_address', models.CharField(default='-', max_length=255, verbose_name='street address')),
                ('phone_number', models.CharField(blank=True, default='-', max_length=10, verbose_name='phone number')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='date of birth')),
                ('gender', models.CharField(blank=True, choices=[('m', 'Male'), ('f', 'Female'), ('n', 'Other')], default='n', max_length=1)),
                ('avatar_img', models.TextField(blank=True, max_length=100, null=True, verbose_name='Avatar')),
                ('bio', models.TextField(blank=True, default='-', verbose_name='bio')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_visible', models.BooleanField(default=False, help_text='Should people be able to see your profile?', verbose_name='Profile visible')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical custom user',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]