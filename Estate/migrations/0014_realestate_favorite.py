# Generated by Django 3.0.2 on 2020-02-01 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Estate', '0013_auto_20200201_1921'),
    ]

    operations = [
        migrations.AddField(
            model_name='realestate',
            name='favorite',
            field=models.BooleanField(default=False, null=True),
        ),
    ]