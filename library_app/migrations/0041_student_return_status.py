# Generated by Django 4.0.3 on 2022-03-25 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0040_student_charges'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='return_status',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
