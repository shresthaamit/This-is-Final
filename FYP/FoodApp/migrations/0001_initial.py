# Generated by Django 3.2.6 on 2022-02-05 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('menuID', models.IntegerField(primary_key=True, serialize=False)),
                ('menuDetail', models.TextField()),
                ('slug', models.SlugField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProductName', models.CharField(max_length=30)),
                ('ProductDetail', models.TextField()),
                ('ProductImage', models.ImageField(upload_to='images/')),
                ('slug', models.SlugField(max_length=30, unique=True)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
