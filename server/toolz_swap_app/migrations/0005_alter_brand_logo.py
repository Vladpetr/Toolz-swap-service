# Generated by Django 3.2.9 on 2021-12-11 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toolz_swap_app', '0004_auto_20211211_0853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='logo',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
