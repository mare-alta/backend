# Generated by Django 3.0 on 2019-12-08 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='flag',
            field=models.BooleanField(default=False),
        ),
    ]
