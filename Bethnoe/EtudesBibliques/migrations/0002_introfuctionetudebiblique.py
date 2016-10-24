# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-23 13:03
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EtudesBibliques', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IntrofuctionEtudeBiblique',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', ckeditor.fields.RichTextField()),
                ('titre', models.CharField(blank=True, max_length=250)),
                ('slug', models.SlugField()),
            ],
        ),
    ]
