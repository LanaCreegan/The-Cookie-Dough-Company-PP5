# Generated by Django 3.2.22 on 2023-10-24 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_rename_has_box_size_product_is_filled'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='is_filled',
        ),
    ]