# Generated by Django 4.0.2 on 2022-12-30 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_featuredproducts_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
    ]