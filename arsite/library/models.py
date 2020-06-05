"""Library models."""

# django
from django.db import models
from django.utils import timezone


class Tag(models.Model):
    """Tag model for video tags."""

    name = models.CharField(max_length=16)

    def __str__(self):
        return self.name


class Video(models.Model):
    """Video model for storing metadata."""

    title = models.CharField(default="None", max_length=128)
    retrieved = models.DateTimeField(default=timezone.now)  # auto_now_add=True
    updated = models.DateTimeField(default=timezone.now)  # auto_now=True
    idd = models.CharField(default="None", max_length=32)
    thumbnail = models.URLField(max_length=256, default="")
    author = models.CharField(default="None", max_length=64)
    published = models.DateField()
    description = models.TextField()
    duration = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    rating = models.DecimalField(decimal_places=2, max_digits=3, default=0.00)
    comment_count = models.IntegerField(default=0)
    face_score = models.DecimalField(decimal_places=2, max_digits=3, default=0.00)

    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title


class SearchQuery(models.Model):
    """Query model to store user queries."""

    query = models.CharField(default="None", max_length=128)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.query
