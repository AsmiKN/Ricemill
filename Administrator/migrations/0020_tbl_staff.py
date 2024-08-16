# Generated by Django 5.0.2 on 2024-03-11 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Administrator', '0019_tbl_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_id', models.CharField(max_length=50)),
                ('staff_name', models.CharField(max_length=50)),
                ('staff_contact', models.CharField(max_length=50)),
                ('staff_email', models.CharField(max_length=50)),
                ('staff_address', models.CharField(max_length=50)),
                ('staff_photo', models.FileField(upload_to='Assets/UserPhoto/')),
            ],
        ),
    ]
