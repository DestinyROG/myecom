# Generated by Django 4.1.5 on 2023-02-14 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewApp', '0008_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('laptops', 'laptops'), ('shoes', 'shoes'), ('fashions', 'fashions')], max_length=255),
        ),
    ]
