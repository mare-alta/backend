# Generated by Django 3.0 on 2019-12-08 04:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('desc', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_hash', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=100)),
                ('level', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Level')),
            ],
        ),
    ]
