# Generated by Django 3.2.3 on 2021-06-03 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apppics', '0006_alter_image_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='category',
        ),
        migrations.RemoveField(
            model_name='image',
            name='location',
        ),
    ]
