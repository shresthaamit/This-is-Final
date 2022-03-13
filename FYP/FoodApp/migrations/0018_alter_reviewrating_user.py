# Generated by Django 3.2.6 on 2022-02-21 05:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('FoodApp', '0017_alter_reviewrating_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewrating',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
