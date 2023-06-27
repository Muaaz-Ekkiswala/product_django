# Generated by Django 3.2 on 2023-06-26 05:47

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=255, verbose_name='employee_first_name')),
                ('last_name', models.CharField(max_length=255, verbose_name='employee_last_name')),
                ('address', models.TextField(verbose_name='employee_address')),
            ],
            options={
                'db_table': 'Staff',
            },
        ),
    ]
