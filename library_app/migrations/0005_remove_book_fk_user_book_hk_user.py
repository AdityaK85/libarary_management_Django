# Generated by Django 4.0.2 on 2022-03-10 07:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0004_alter_book_master_author_book'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='fk_user',
        ),
        migrations.AddField(
            model_name='book',
            name='hk_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='library_app.book_master'),
        ),
    ]
