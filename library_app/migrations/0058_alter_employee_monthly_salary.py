# Generated by Django 4.0.3 on 2022-03-31 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0057_rename_designation_employee_destination_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='monthly_salary',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
