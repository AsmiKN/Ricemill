# Generated by Django 5.0.2 on 2024-03-19 18:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Administrator', '0031_tbl_unit'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_newproduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('newproduct_name', models.CharField(max_length=50)),
                ('newproduct_price', models.CharField(max_length=50)),
                ('newproduct_details', models.CharField(max_length=50)),
                ('newproduct_stock', models.CharField(max_length=50)),
                ('newproduct_photo', models.FileField(upload_to='Assets/newproductphoto/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Administrator.tbl_category')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Administrator.tbl_unit')),
            ],
        ),
    ]
