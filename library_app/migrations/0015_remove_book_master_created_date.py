# Generated by Django 4.0.3 on 2022-03-15 05:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0014_remove_book_master_date_remove_book_master_month'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book_master',
            name='created_date',
        ),
    ]
