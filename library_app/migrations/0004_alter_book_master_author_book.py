# Generated by Django 4.0.2 on 2022-03-10 07:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0003_book_master'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book_master',
            name='author',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(blank=True, max_length=50, null=True)),
                ('author', models.CharField(blank=True, max_length=50, null=True)),
                ('dop', models.DateField(blank=True, max_length=50, null=True)),
                ('category', models.CharField(blank=True, max_length=50, null=True)),
                ('condition', models.CharField(blank=True, max_length=50, null=True)),
                ('price', models.CharField(blank=True, max_length=50, null=True)),
                ('fk_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='library_app.user')),
            ],
        ),
    ]
