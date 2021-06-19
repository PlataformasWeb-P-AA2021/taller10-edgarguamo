# Generated by Django 3.2.4 on 2021-06-19 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parroquia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre de la parroquia')),
                ('tipo', models.CharField(choices=[('Urbana', 'urbana'), ('Rural', 'rural')], max_length=8)),
            ],
            options={
                'verbose_name_plural': 'Las Parroquias',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Barrio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150, verbose_name='nombre del Barrio')),
                ('num_viviendas', models.CharField(max_length=2, verbose_name='Número de Viviendas')),
                ('num_parques', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)], verbose_name='Número parques')),
                ('num_edificios', models.IntegerField(verbose_name='Número de Edificios')),
                ('parroquia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lasparroquias', to='ordenamiento.parroquia')),
            ],
            options={
                'verbose_name_plural': 'Los Barrios',
                'ordering': ['nombre'],
            },
        ),
    ]
