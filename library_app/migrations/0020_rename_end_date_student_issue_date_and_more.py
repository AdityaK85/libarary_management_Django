# Generated by Django 4.0.3 on 2022-03-16 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0019_student_book_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='end_date',
            new_name='issue_date',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='start_date',
            new_name='till_date',
        ),
    ]