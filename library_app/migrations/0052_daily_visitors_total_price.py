# Generated by Django 4.0.3 on 2022-03-28 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0051_rename_payment_status_daily_visitors_payment_status_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='daily_visitors',
            name='total_price',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
