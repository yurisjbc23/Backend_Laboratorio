# Generated by Django 3.0.7 on 2021-09-26 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Program',
            fields=[
                ('code', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('number_semesters', models.SmallIntegerField(default=1)),
                ('state', models.CharField(default='A', max_length=1)),
            ],
            options={
                'db_table': 'Program',
            },
        ),
        migrations.CreateModel(
            name='Pensum',
            fields=[
                ('code', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=1000, unique=True)),
                ('expiration_date', models.DateField()),
                ('date_issue', models.DateField()),
                ('state', models.CharField(default='A', max_length=1)),
                ('program_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyecto.Program')),
            ],
            options={
                'db_table': 'Pensum',
            },
        ),
    ]