# Generated by Django 4.0.3 on 2022-03-17 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0023_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='designation',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='doj',
            field=models.DateField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]