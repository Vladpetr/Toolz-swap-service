# Generated by Django 3.2.9 on 2021-12-16 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toolz_swap_app', '0018_auto_20211216_0833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listingimage',
            name='item_image',
            field=models.ImageField(blank=True, null=True, upload_to='listing_images'),
        ),
        migrations.AlterField(
            model_name='listingimage',
            name='top_image',
            field=models.BooleanField(default=False),
        ),
    ]
