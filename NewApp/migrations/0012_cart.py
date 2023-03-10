# Generated by Django 4.1.5 on 2023-02-15 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewApp', '0011_remove_product_urlname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('product_image', models.ImageField(upload_to='Media\\Cart_Image')),
                ('quantity', models.IntegerField(default=1)),
                ('price', models.FloatField()),
            ],
        ),
    ]
