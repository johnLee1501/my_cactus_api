# Generated by Django 3.1.5 on 2021-01-28 03:14

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CactusModel',
            fields=[
                ('cactus_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('cactus_name', models.CharField(max_length=50)),
                ('cactus_class', models.CharField(blank=True, max_length=50, null=True)),
                ('cactus_description', models.TextField(blank=True, max_length=200, null=True)),
                ('cactus_picture', models.ImageField(unique=True, upload_to='pictures')),
            ],
            options={
                'db_table': 'cactus',
            },
        ),
    ]
