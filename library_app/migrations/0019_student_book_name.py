# Generated by Django 4.0.3 on 2022-03-16 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0018_rename_issue_date_student_end_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='book_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]