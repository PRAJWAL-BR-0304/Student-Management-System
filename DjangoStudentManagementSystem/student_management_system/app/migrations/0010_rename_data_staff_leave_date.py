# Generated by Django 5.1.3 on 2024-12-18 18:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_staff_leave'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staff_leave',
            old_name='data',
            new_name='date',
        ),
    ]
