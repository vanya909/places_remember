# Generated by Django 4.0.2 on 2022-03-04 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
    ]
