# Generated by Django 5.0.2 on 2024-03-11 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Administrator', '0017_tbl_gallery_delete_tbl_galleryproduct'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier_id', models.CharField(max_length=50)),
                ('supplier_name', models.CharField(max_length=50)),
                ('supplier_contact', models.CharField(max_length=50)),
                ('supplier_email', models.CharField(max_length=50)),
                ('supplier_address', models.CharField(max_length=50)),
                ('GstNo', models.CharField(max_length=50)),
            ],
        ),
    ]
