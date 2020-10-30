# Generated by Django 3.1.1 on 2020-10-30 21:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modulo2', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=100)),
                ('abbreviation', models.CharField(max_length=10)),
                ('status', models.BooleanField(default=True)),
                ('creation_date', models.DateTimeField()),
                ('modification_date', models.DateTimeField()),
                ('id_pais', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modulo2.paises')),
            ],
        ),
        migrations.CreateModel(
            name='afiliados',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('cellphone_number', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=100)),
                ('status', models.BooleanField(default=True)),
                ('creation_date', models.DateTimeField()),
                ('modification_date', models.DateTimeField()),
                ('id_ciudad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modulo2.ciudades')),
            ],
        ),
    ]
