# Generated by Django 3.0.6 on 2020-05-30 22:04

# django
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="SearchQuery",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("query", models.CharField(default="None", max_length=128)),
                ("count", models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name="Video",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(default="None", max_length=128)),
                ("retrieved", models.DateTimeField(default=django.utils.timezone.now)),
                ("updated", models.DateTimeField(default=django.utils.timezone.now)),
                ("idd", models.CharField(default="None", max_length=32)),
                ("thumbnail", models.URLField(default="", max_length=256)),
                ("author", models.CharField(default="None", max_length=64)),
                ("date", models.DateField()),
                ("description", models.TextField()),
                ("duration", models.IntegerField(default=0)),
                ("views", models.IntegerField(default=0)),
                (
                    "rating",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=3),
                ),
                ("commentCount", models.IntegerField(default=0)),
                (
                    "faceScore",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=3),
                ),
                ("tags", models.ManyToManyField(to="library.Tag")),
            ],
        ),
    ]
