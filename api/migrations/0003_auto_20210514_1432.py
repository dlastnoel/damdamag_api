# Generated by Django 3.2.2 on 2021-05-14 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_case_post_request_resident'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='code',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='request',
            name='status',
            field=models.CharField(default='pending', max_length=255),
        ),
    ]
