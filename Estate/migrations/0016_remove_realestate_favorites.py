# Generated by Django 3.0.2 on 2020-02-02 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Estate', '0015_auto_20200202_1224'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='realestate',
            name='favorites',
        ),
    ]
