# Generated by Django 3.0.5 on 2024-01-06 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0009_result_corrects'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='corrects',
        ),
    ]
