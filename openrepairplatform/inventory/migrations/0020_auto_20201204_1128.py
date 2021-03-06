# Generated by Django 2.2.4 on 2020-12-04 10:28

from django.db import migrations, models
import django.db.models.deletion
import openrepairplatform.fields


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0019_auto_20201127_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalstuff',
            name='device',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='inventory.Device', verbose_name="Type d'appareil"),
        ),
        migrations.AlterField(
            model_name='historicalstuff',
            name='information',
            field=openrepairplatform.fields.CleanHTMLField(blank=True, help_text="D'où vient-il, a t'il des caractéristiques spéciales... bref, tout ce qui peut le décrire", null=True, verbose_name='Information optionnelles sur cet appareil'),
        ),
        migrations.AlterField(
            model_name='historicalstuff',
            name='place',
            field=models.ForeignKey(blank=True, db_constraint=False, help_text="Où se trouve l'appareil ?", null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='location.Place', verbose_name='Localisation'),
        ),
        migrations.AlterField(
            model_name='historicalstuff',
            name='state',
            field=models.CharField(choices=[('B', 'En panne'), ('W', 'Fonctionnel'), ('D', 'Désassemblé'), ('F', 'En réparation'), ('T', 'Evaporé'), ('P', 'Partiel')], default='B', max_length=1, verbose_name='Etat'),
        ),
        migrations.AlterField(
            model_name='intervention',
            name='reasoning',
            field=models.ForeignKey(blank=True, help_text='Quel en est (ou serait) la cause ?', null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.Reasoning'),
        ),
        migrations.AlterField(
            model_name='stuff',
            name='device',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='stuffs', to='inventory.Device', verbose_name="Type d'appareil"),
        ),
        migrations.AlterField(
            model_name='stuff',
            name='information',
            field=openrepairplatform.fields.CleanHTMLField(blank=True, help_text="D'où vient-il, a t'il des caractéristiques spéciales... bref, tout ce qui peut le décrire", null=True, verbose_name='Information optionnelles sur cet appareil'),
        ),
        migrations.AlterField(
            model_name='stuff',
            name='place',
            field=models.ForeignKey(blank=True, help_text="Où se trouve l'appareil ?", null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='place', to='location.Place', verbose_name='Localisation'),
        ),
        migrations.AlterField(
            model_name='stuff',
            name='state',
            field=models.CharField(choices=[('B', 'En panne'), ('W', 'Fonctionnel'), ('D', 'Désassemblé'), ('F', 'En réparation'), ('T', 'Evaporé'), ('P', 'Partiel')], default='B', max_length=1, verbose_name='Etat'),
        ),
    ]
