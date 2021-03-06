# Generated by Django 2.1.2 on 2018-10-20 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('incidentes', '0002_auto_20181020_0802'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('descripción', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buenos', models.IntegerField()),
                ('dañados', models.IntegerField()),
                ('nombre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='incidentes.Equipos')),
            ],
        ),
        migrations.AddField(
            model_name='categoria',
            name='relevancia',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='nombre',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='grupo',
            name='nombre',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='incidentes.Usuario'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='apellido',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nombre',
            field=models.CharField(max_length=25),
        ),
        migrations.AddField(
            model_name='ticket',
            name='equipo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='incidentes.Equipos'),
        ),
    ]
