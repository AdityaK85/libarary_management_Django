# Generated by Django 4.0.3 on 2022-03-15 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0015_remove_book_master_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='book_master',
            name='created_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
