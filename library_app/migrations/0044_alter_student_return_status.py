# Generated by Django 4.0.3 on 2022-03-25 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0043_alter_student_return_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='return_status',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
