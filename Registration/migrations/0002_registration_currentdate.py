# Generated by Django 4.2.3 on 2023-08-23 14:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='currentdate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
