# Generated by Django 3.2.9 on 2021-11-21 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('toolz_swap_app', '0002_auto_20211117_2210'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tool',
            options={'ordering': ['toolName']},
        ),
    ]
