# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-02 13:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('EgliseBethnoe', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageBackgroud',
            fields=[
                ('imageaccueil_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='EgliseBethnoe.ImageAccueil')),
            ],
            bases=('EgliseBethnoe.imageaccueil',),
        ),
    ]
