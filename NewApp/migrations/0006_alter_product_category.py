# Generated by Django 4.1.5 on 2023-02-14 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewApp', '0005_alter_category_urlname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Shoes', 'Shoes'), ('Laptop', 'Laptop')], max_length=255, null=True),
        ),
    ]
