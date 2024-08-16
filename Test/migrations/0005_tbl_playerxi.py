# Generated by Django 5.0.2 on 2024-02-29 06:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Test', '0004_tbl_matchschedule'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_playerxi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matchschedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Test.tbl_matchschedule')),
                ('playerdetails', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Test.tbl_playerdetails')),
            ],
        ),
    ]
