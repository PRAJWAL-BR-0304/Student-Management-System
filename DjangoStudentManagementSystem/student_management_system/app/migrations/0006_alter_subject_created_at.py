# Generated by Django 5.1.3 on 2024-11-30 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]