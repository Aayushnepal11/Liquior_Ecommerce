# Generated by Django 4.0.2 on 2022-10-08 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_featuredproducts_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='featuredproducts',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='./img'),
        ),
    ]
