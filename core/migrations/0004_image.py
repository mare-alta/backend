# Generated by Django 3.0 on 2019-12-08 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20191208_0556'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.TextField()),
                ('appropriate', models.CharField(max_length=100)),
                ('insert_date', models.DateTimeField(auto_now=True)),
                ('complaint', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Complaint')),
            ],
        ),
    ]
