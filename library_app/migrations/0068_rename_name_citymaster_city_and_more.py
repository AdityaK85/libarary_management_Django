# Generated by Django 4.0.3 on 2022-05-31 09:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0067_citymaster_delete_city_master'),
    ]

    operations = [
        migrations.RenameField(
            model_name='citymaster',
            old_name='name',
            new_name='city',
        ),
        migrations.RemoveField(
            model_name='citymaster',
            name='state_id',
        ),
    ]
