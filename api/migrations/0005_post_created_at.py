# Generated by Django 3.2.2 on 2021-05-14 07:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_official_managers'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='created_at',
            field=models.DateField(auto_now_add=True, default=datetime.datetime(2021, 5, 14, 7, 39, 27, 988978, tzinfo=utc)),
            preserve_default=False,
        ),
    ]