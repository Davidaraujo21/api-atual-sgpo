# Generated by Django 3.2.4 on 2022-02-07 04:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_entrada_arquivo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entrada',
            name='arquivo',
        ),
    ]