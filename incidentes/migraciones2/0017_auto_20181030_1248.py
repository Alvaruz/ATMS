# Generated by Django 2.1.2 on 2018-10-30 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incidentes', '0016_auto_20181030_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='editado_por',
            field=models.ManyToManyField(blank=True, choices=[(1, '--------'), (2, 'Jose Cassanello'), (3, 'Emilio Yegros'), (4, 'Gustavo González'), (5, 'Manuel Gamarra'), (6, 'Leandro Argañaraz'), (7, 'Félix Mendoza'), (8, 'Jorge Colmán'), (9, 'Aida Franco'), (10, 'Ing. Rolón'), (11, 'Victor Peña'), (12, 'Alvaro Cardenas')], default='', related_name='nombre2', to='incidentes.Usuario'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='usuario',
            field=models.ManyToManyField(choices=[(1, '--------'), (2, 'Jose Cassanello'), (3, 'Emilio Yegros'), (4, 'Gustavo González'), (5, 'Manuel Gamarra'), (6, 'Leandro Argañaraz'), (7, 'Félix Mendoza'), (8, 'Jorge Colmán'), (9, 'Aida Franco'), (10, 'Ing. Rolón'), (11, 'Victor Peña'), (12, 'Alvaro Cardenas')], default='', to='incidentes.Usuario'),
        ),
    ]
