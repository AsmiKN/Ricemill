# Generated by Django 5.0.2 on 2024-03-25 05:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Administrator', '0052_delete_tbl_supplier'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier_name', models.CharField(max_length=50)),
                ('supplier_contact', models.CharField(max_length=50)),
                ('supplier_email', models.CharField(max_length=50)),
                ('supplier_address', models.CharField(max_length=50)),
                ('supplier_gstno', models.CharField(max_length=50)),
                ('supplier_password', models.CharField(max_length=50)),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Administrator.tbl_place')),
            ],
        ),
    ]
