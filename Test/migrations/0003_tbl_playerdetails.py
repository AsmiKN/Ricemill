# Generated by Django 5.0.2 on 2024-02-28 06:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Test', '0002_tbl_playercategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_playerdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playerdetails_name', models.CharField(max_length=50)),
                ('playerdetails_dob', models.CharField(max_length=50)),
                ('playerdetails_photo', models.FileField(upload_to='Assets/UserPhoto/')),
                ('playerdetails_status', models.IntegerField(default='0')),
                ('playercategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Test.tbl_playercategory')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Test.tbl_team')),
            ],
        ),
    ]
