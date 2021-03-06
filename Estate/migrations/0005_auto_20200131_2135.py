# Generated by Django 3.0.2 on 2020-01-31 21:35

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Estate', '0004_profile_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='search_location',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user_location',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326),
        ),
    ]
