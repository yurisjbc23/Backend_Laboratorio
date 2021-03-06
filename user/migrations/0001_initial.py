# Generated by Django 3.0.7 on 2021-09-28 06:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('proyecto', '0005_auto_20210928_0224'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=20)),
                ('Photo', models.ImageField(default='pictures/default.png', max_length=255, upload_to='pictures/%y/%m/%d')),
                ('status', models.BooleanField(default=True)),
                ('program_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyecto.Program')),
            ],
            options={
                'db_table': 'Employee',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'Role',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Correo electronico')),
                ('password', models.CharField(max_length=20)),
                ('Employee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.Employee')),
                ('Role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Role')),
            ],
            options={
                'db_table': 'User',
            },
        ),
    ]
