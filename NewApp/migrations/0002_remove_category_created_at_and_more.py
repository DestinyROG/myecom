# Generated by Django 4.1.5 on 2023-02-09 05:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NewApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='category',
            name='description',
        ),
        migrations.RemoveField(
            model_name='category',
            name='meta_description',
        ),
        migrations.RemoveField(
            model_name='category',
            name='meta_keywords',
        ),
        migrations.RemoveField(
            model_name='category',
            name='meta_title',
        ),
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='category',
            name='status',
        ),
        migrations.RemoveField(
            model_name='category',
            name='trending',
        ),
        migrations.RemoveField(
            model_name='product',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='product',
            name='meta_description',
        ),
        migrations.RemoveField(
            model_name='product',
            name='meta_keywords',
        ),
        migrations.RemoveField(
            model_name='product',
            name='meta_title',
        ),
        migrations.RemoveField(
            model_name='product',
            name='small_description',
        ),
        migrations.RemoveField(
            model_name='product',
            name='status',
        ),
        migrations.RemoveField(
            model_name='product',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='product',
            name='trending',
        ),
    ]
