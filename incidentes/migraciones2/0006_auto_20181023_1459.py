# Generated by Django 2.1.2 on 2018-10-23 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('incidentes', '0005_auto_20181022_1004'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categoria',
            old_name='descripción',
            new_name='descripcion',
        ),
        migrations.RenameField(
            model_name='equipos',
            old_name='descripción',
            new_name='descripcion',
        ),
        migrations.RenameField(
            model_name='estado',
            old_name='descripción',
            new_name='descripcion',
        ),
        migrations.RenameField(
            model_name='grupo',
            old_name='descripción',
            new_name='descripcion',
        ),
    ]
