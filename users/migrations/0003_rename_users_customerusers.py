# Generated by Django 4.0.2 on 2023-01-22 03:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_users_options'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Users',
            new_name='CustomerUsers',
        ),
    ]
