# Generated by Django 4.0.2 on 2023-01-28 02:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0021_alter_product_index_together'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='Category',
            new_name='category',
        ),
    ]