# Generated by Django 3.2.3 on 2021-06-01 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_location', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ['image_location'],
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(max_length=30)),
                ('image_description', models.CharField(max_length=300)),
                ('image', models.ImageField(blank=True, upload_to='media/')),
                ('category', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='apppics.category')),
                ('location', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='apppics.location')),
            ],
        ),
    ]
