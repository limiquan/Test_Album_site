# Generated by Django 3.2.5 on 2024-07-08 09:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='photo/%Y/%m%d/')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
