# Generated by Django 4.2.3 on 2023-08-21 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('fname', models.CharField(max_length=50)),
                ('study', models.CharField(max_length=100)),
                ('course', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=50)),
                ('address', models.TextField()),
            ],
        ),
    ]