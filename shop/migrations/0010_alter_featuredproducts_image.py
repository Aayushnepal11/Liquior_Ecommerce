# Generated by Django 4.0.2 on 2023-01-20 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_alter_contact_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='featuredproducts',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='../img'),
        ),
    ]
