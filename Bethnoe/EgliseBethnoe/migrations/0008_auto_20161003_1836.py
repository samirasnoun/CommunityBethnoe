# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-03 16:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EgliseBethnoe', '0007_textdirigenteglisebethnoe'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdresseSimple',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_rue', models.IntegerField(blank=True)),
                ('type_rue', models.CharField(choices=[('Bd', 'Boulevard'), ('R.', 'Rue')], default='R.', max_length=2)),
                ('nom_rue', models.CharField(blank=True, max_length=150)),
                ('ville', models.CharField(blank=True, max_length=150)),
                ('code_postale', models.CharField(default='75', max_length=150)),
                ('pays', models.CharField(default='France', max_length=150)),
            ],
            options={
                'verbose_name': 'Adresse de contact de l eglise',
                'verbose_name_plural': 'Adresse de contact de l eglise',
            },
        ),
        migrations.AlterModelOptions(
            name='adresse',
            options={'verbose_name': 'Adresse de contact de l eglise', 'verbose_name_plural': 'Adresse de contact de l eglise'},
        ),
    ]
