# Generated by Django 3.0.2 on 2020-02-01 19:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Estate', '0012_auto_20200201_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realestateimages',
            name='estate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pictures', to='Estate.RealEstate'),
        ),
    ]
