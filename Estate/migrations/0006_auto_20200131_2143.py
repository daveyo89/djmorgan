# Generated by Django 3.0.2 on 2020-01-31 21:43

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Estate', '0005_auto_20200131_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(default='default.jpg', storage=django.core.files.storage.FileSystemStorage(location='/static/media/profile_pics'), upload_to=''),
        ),
    ]
