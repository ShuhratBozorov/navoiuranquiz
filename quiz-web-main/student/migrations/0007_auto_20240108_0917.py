# Generated by Django 3.0.5 on 2024-01-08 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0006_auto_20240106_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='regions',
            field=models.CharField(blank=True, choices=[('region1', 'Navoiyuran'), ('region2', 'Nurobod'), ('region3', 'Zafarobod'), ('region4', 'Uchquduq'), ('region5', 'Uran va noyob ishlab chiqarish markazi')], max_length=20, null=True),
        ),
    ]