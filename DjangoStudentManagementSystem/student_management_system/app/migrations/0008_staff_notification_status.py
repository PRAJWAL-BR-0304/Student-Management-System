# Generated by Django 5.1.3 on 2024-11-30 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_subject_created_at_staff_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff_notification',
            name='status',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
