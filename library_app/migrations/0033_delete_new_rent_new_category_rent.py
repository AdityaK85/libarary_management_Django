# Generated by Django 4.0.3 on 2022-03-24 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0032_new_rent'),
    ]

    operations = [
        migrations.DeleteModel(
            name='New_Rent',
        ),
        migrations.AddField(
            model_name='new_category',
            name='rent',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
