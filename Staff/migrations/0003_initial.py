# Generated by Django 5.0.2 on 2024-04-03 05:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Administrator', '0061_tbl_production'),
        ('Staff', '0002_remove_tbl_productbooking_staff_delete_tbl_cart_and_more'),
        ('Supplier', '0009_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_rawmaterialbooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_date', models.DateField(auto_now_add=True)),
                ('booking_status', models.IntegerField(default='0')),
                ('price', models.CharField(default='0', max_length=40)),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Administrator.tbl_staff')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_qty', models.CharField(max_length=500)),
                ('cart_status', models.IntegerField(default='0')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Supplier.tbl_supplierraw')),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Staff.tbl_rawmaterialbooking')),
            ],
        ),
    ]
