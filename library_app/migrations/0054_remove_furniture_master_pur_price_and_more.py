# Generated by Django 4.0.3 on 2022-03-30 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0053_furniture_master'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='furniture_master',
            name='Pur_price',
        ),
        migrations.RemoveField(
            model_name='furniture_master',
            name='condition',
        ),
        migrations.RemoveField(
            model_name='furniture_master',
            name='electronics',
        ),
        migrations.RemoveField(
            model_name='furniture_master',
            name='fur_dop',
        ),
    ]
