# Generated by Django 4.0.3 on 2022-03-24 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0036_student_difference'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='difference',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]