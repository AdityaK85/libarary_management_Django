# Generated by Django 4.0.3 on 2022-04-04 05:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0058_alter_employee_monthly_salary'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bills_Master',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_type', models.CharField(blank=True, max_length=150, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Bills_Duplicate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_image', models.ImageField(blank=True, null=True, upload_to='Bills_Images/')),
                ('payment_type', models.BooleanField(blank=True, default=False, max_length=100, null=True)),
                ('status', models.BooleanField(blank=True, default=False, max_length=100, null=True)),
                ('fk_bill_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='library_app.bills_master')),
            ],
        ),
    ]
