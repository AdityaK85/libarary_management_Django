# Generated by Django 4.0.3 on 2022-03-22 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0029_alter_student_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='status',
            new_name='request',
        ),
    ]
