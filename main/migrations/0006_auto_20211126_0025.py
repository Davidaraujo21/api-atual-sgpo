# Generated by Django 3.2.4 on 2021-11-26 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_rename_fronteirate_processo_fronteiraate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='macroprocesso',
            name='componentes_vinculados',
            field=models.ManyToManyField(blank=True, related_name='componentesVincAcess', to='main.Componente'),
        ),
        migrations.AlterField(
            model_name='processo',
            name='macroProcessos_vinculados',
            field=models.ManyToManyField(blank=True, related_name='macroProcessoVinc', to='main.MacroProcesso'),
        ),
    ]