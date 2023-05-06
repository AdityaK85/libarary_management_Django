# Generated by Django 4.0.3 on 2022-03-24 07:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0033_delete_new_rent_new_category_rent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='new_category',
            name='rent',
        ),
        migrations.CreateModel(
            name='Rent_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rent', models.CharField(blank=True, max_length=50, null=True)),
                ('hk_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='library_app.new_category')),
            ],
        ),
    ]
