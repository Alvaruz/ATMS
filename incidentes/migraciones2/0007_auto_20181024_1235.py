# Generated by Django 2.1.2 on 2018-10-24 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('incidentes', '0006_auto_20181023_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='fecha',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='incidentes.Usuario'),
        ),
    ]
