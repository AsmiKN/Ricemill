# Generated by Django 5.0.2 on 2024-02-22 05:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Administrator', '0011_tbl_syllabus'),
        ('Guest', '0004_delete_tbl_newuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_newuser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('newuser_name', models.CharField(max_length=150)),
                ('newuser_gender', models.CharField(max_length=150)),
                ('newuser_contact', models.CharField(max_length=100)),
                ('newuser_email', models.CharField(max_length=100)),
                ('newuser_password', models.CharField(max_length=100)),
                ('newuser_address', models.CharField(max_length=100)),
                ('newuser_photo', models.FileField(upload_to='Assets/UserPhoto/')),
                ('newuser_proof', models.FileField(upload_to='Assets/UserProof/')),
                ('newuser_status', models.IntegerField(default='0')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Administrator.tbl_place')),
            ],
        ),
    ]
