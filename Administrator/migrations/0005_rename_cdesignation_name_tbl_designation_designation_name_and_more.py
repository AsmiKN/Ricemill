# Generated by Django 5.0.2 on 2024-02-15 09:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Administrator', '0004_tbl_designation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tbl_designation',
            old_name='cdesignation_name',
            new_name='designation_name',
        ),
        migrations.CreateModel(
            name='tbl_place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_name', models.CharField(max_length=50)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Administrator.tbl_district')),
            ],
        ),
    ]
