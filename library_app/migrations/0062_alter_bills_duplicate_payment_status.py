# Generated by Django 4.0.3 on 2022-04-04 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0061_bills_duplicate_online_var'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bills_duplicate',
            name='payment_status',
            field=models.CharField(blank=True, default=False, max_length=100, null=True),
        ),
    ]
