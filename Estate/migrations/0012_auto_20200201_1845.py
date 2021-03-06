# Generated by Django 3.0.2 on 2020-02-01 18:45

import django.core.files.storage
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Estate', '0011_auto_20200201_1826'),
    ]

    operations = [
        migrations.CreateModel(
            name='RealEstateImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.PositiveSmallIntegerField(default=0)),
                ('image', models.ImageField(upload_to=django.core.files.storage.FileSystemStorage(location='/root/PycharmProjects/Morgan/Morgan/media'))),
                ('estate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Estate.RealEstate')),
            ],
            options={
                'ordering': ['position'],
            },
        ),
        migrations.DeleteModel(
            name='RealEstateImage',
        ),
    ]
