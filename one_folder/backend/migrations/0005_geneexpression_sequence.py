# Generated by Django 3.2.4 on 2021-06-05 01:59

import backend.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_alter_patient_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sequence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField(auto_now=True, verbose_name='Submission date')),
                ('direction', models.CharField(choices=[('Forward', 'Forward'), ('Reverse', 'Reverse'), ('Single', 'Single')], max_length=50, verbose_name='Direction')),
                ('sequnce', models.FileField(blank=True, upload_to=backend.models.upload_to, verbose_name='Sequence')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.patient', verbose_name='Patient')),
            ],
        ),
        migrations.CreateModel(
            name='GeneExpression',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gene', models.CharField(max_length=50, verbose_name='Gene')),
                ('expression', models.DecimalField(decimal_places=3, max_digits=10, verbose_name='Expression level')),
                ('sequence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.sequence', verbose_name='Sequence')),
            ],
        ),
    ]
