# Generated by Django 4.1.5 on 2023-02-09 05:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NewApp', '0002_remove_category_created_at_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='slug',
            new_name='urlname',
        ),
    ]
