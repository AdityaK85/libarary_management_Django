# Generated by Django 4.0.3 on 2022-03-26 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0047_alter_daily_visitors_contact_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='rent_category',
            name='hourly_price',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]