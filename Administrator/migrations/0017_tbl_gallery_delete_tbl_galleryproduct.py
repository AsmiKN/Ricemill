# Generated by Django 5.0.2 on 2024-02-27 05:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Administrator', '0016_tbl_galleryproduct'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gallery_description', models.CharField(max_length=50)),
                ('gallery_photo', models.FileField(upload_to='Assets/UserPhoto/')),
                ('gallery_status', models.IntegerField(default='0')),
                ('product_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Administrator.tbl_product')),
            ],
        ),
        migrations.DeleteModel(
            name='tbl_galleryproduct',
        ),
    ]
