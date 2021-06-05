# Generated by Django 3.2.4 on 2021-06-05 01:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('national_id', models.CharField(max_length=50, unique=True, verbose_name='National id')),
                ('city', models.CharField(max_length=50, verbose_name='city')),
                ('nationality', models.CharField(max_length=50, verbose_name='Nationality')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=50, verbose_name='Gender')),
                ('birthdate', models.DateField(verbose_name='Birthdate')),
                ('first_name', models.CharField(max_length=50, verbose_name='Firtst Name')),
                ('last_name', models.CharField(max_length=50, verbose_name='Last Name')),
                ('onset_date', models.DateField(auto_now=True, verbose_name='Onset Date')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.doctor', verbose_name='Doctor')),
            ],
        ),
    ]
