# Generated by Django 3.2.9 on 2021-11-17 21:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('toolz_swap_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('expires', models.DateTimeField()),
                ('lenderId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('toolName', models.CharField(max_length=200)),
                ('toolModel', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('available', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Swaps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('expires', models.DateTimeField()),
                ('borrowerId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('listingId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='toolz_swap_app.listing')),
                ('toolId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='toolz_swap_app.tool')),
            ],
        ),
        migrations.AddField(
            model_name='listing',
            name='toolId',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='toolz_swap_app.tool'),
        ),
    ]
