# Generated by Django 3.0.6 on 2020-05-30 23:15

# django
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("library", "0004_auto_20200530_1846"),
    ]

    operations = [
        migrations.AlterField(
            model_name="video",
            name="updated",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
