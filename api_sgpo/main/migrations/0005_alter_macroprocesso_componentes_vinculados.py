# Generated by Django 3.2.4 on 2021-06-25 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_processo_macroprocessos_vinculados'),
    ]

    operations = [
        migrations.AlterField(
            model_name='macroprocesso',
            name='componentes_vinculados',
            field=models.ManyToManyField(blank=True, null=True, related_name='componentesVincAcess', to='main.Componente'),
        ),
    ]