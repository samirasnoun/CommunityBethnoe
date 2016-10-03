# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-02 13:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EgliseBethnoe', '0004_adresse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adresse',
            name='code_dep',
            field=models.CharField(choices=[(b'1', b'Ain  '), (b'2', b'Aisne  '), (b'3', b'Allier  '), (b'4', b'Alpes-de-Haute-Provence  '), (b'5', b'Hautes-Alpes  '), (b'6', b'Alpes-Martimes  '), (b'7', b'Ard\xc3\xa8che  '), (b'8', b'Ardennes  '), (b'9', b'Ari\xc3\xa8ge  '), (b'10', b'Aube  '), (b'11', b'Aude  '), (b'12', b'Aveyron  '), (b'13', b'Bouches-du-Rh\xc3\xb4ne  '), (b'14', b'Calvados  '), (b'15', b'Cantal  '), (b'16', b'Charente  '), (b'17', b'Charente-Maritime  '), (b'18', b'Cher  '), (b'19', b'Corr\xc3\xa8ze  '), (b'2A', b'Corse-du-Sud  '), (b'2B', b'Haute-Corse  '), (b'21', b"C\xc3\xb4te-d'Or  "), (b'22', b"C\xc3\xb4tes-d'Armor  "), (b'23', b'Creuse  '), (b'24', b'Dordogne  '), (b'25', b'Doubs  '), (b'26', b'Dr\xc3\xb4me  '), (b'27', b'Eure  '), (b'28', b'Eure-et-Loir  '), (b'29', b'Finist\xc3\xa8re  '), (b'30', b'Gard  '), (b'31', b'Haute-Garonne  '), (b'32', b'Gers  '), (b'33', b'Gironde  '), (b'34', b'H\xc3\xa9rault  '), (b'35', b'Ille-et-Vilaine  '), (b'36', b'Indre  '), (b'37', b'Indre-et-Loire  '), (b'38', b'Is\xc3\xa8re  '), (b'39', b'Jura  '), (b'40', b'Landes  '), (b'41', b'Loir-et-Cher  '), (b'42', b'Loire  '), (b'43', b'Haute-Loire  '), (b'44', b'Loire-Atlantique  '), (b'45', b'Loiret  '), (b'46', b'Lot  '), (b'47', b'Lot-et-Garonne  '), (b'48', b'Loz\xc3\xa8re  '), (b'49', b'Maine-et-Loire  '), (b'50', b'Manche  '), (b'51', b'Marne  '), (b'52', b'Haute-Marne  '), (b'53', b'Mayenne  '), (b'54', b'Meurthe-et-Moselle  '), (b'55', b'Meuse  '), (b'56', b'Morbihan  '), (b'57', b'Moselle  '), (b'58', b'Ni\xc3\xa8vre  '), (b'59', b'Nord  '), (b'60', b'Oise  '), (b'61', b'Orne  '), (b'62', b'Pas-de-Calais  '), (b'63', b'Puy-de-D\xc3\xb4me  '), (b'64', b'Pyr\xc3\xa9n\xc3\xa9es-Atlantique  '), (b'65', b'Hautes-Pyr\xc3\xa9n\xc3\xa9es  '), (b'66', b'Pyr\xc3\xa9n\xc3\xa9es-Orientales  '), (b'67', b'Bas-Rhin  '), (b'68', b'Haut-Rhin  '), (b'69', b'Rh\xc3\xb4ne  '), (b'70', b'Haute-Sa\xc3\xb4ne  '), (b'71', b'Sa\xc3\xb4ne-et-Loire  '), (b'72', b'Sarthe  '), (b'73', b'Savoie  '), (b'74', b'Haute-Savoie  '), (b'75', b'Paris  '), (b'76', b'Seine-Maritime  '), (b'77', b'Seine-et-Marne  '), (b'78', b'Yvelines  '), (b'79', b'Deux-S\xc3\xa8vres  '), (b'80', b'Somme  '), (b'81', b'Tarn  '), (b'82', b'Tarn-et-Garonne  '), (b'83', b'Var  '), (b'84', b'Vaucluse  '), (b'85', b'Vend\xc3\xa9e  '), (b'86', b'Vienne  '), (b'87', b'Haute-Vienne  '), (b'88', b'Vosges  '), (b'89', b'Yonne  '), (b'91', b'Essonne  '), (b'92', b'Hauts-de-Seine  '), (b'93', b'Seine-St-Denis  '), (b'94', b'Val-de-Marne  '), (b'95', b"Val-d'Oise  "), (b'971', b'Guadeloupe  '), (b'973', b'Guyane  '), (b'975', b'St-Pierre-et-Miquelon  '), (b'972', b'Martinique  '), (b'974', b'La R\xc3\xa9union '), (b'976', b'Mayotte  '), (b'984', b'Terres-Australes et Antarctiques'), (b'987', b'Polyn\xc3\xa9sie Fran\xc3\xa7aise '), (b'986', b'Wallis-et-Futuna  '), (b'988', b'Nouvelle-Cal\xc3\xa9donie  ')], default='75', max_length=150),
        ),
    ]
