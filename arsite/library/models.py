from django.db import models
from django.utils import timezone



class Tag(models.Model):
    name = models.CharField(max_length=16)

    def __str__(self):
        return self.name


class Video(models.Model):
    title = models.CharField(default='None', max_length=128)
    retrieved = models.DateTimeField(default=timezone.now)      # auto_now_add=True
    updated = models.DateTimeField(default=timezone.now)        #auto_now=True
    idd = models.CharField(default='None', max_length=32)
    thumbnail = models.URLField(max_length=256, default='')
    author = models.CharField(default='None', max_length=64)
    published = models.DateField()
    description = models.TextField()
    duration = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    rating = models.DecimalField(decimal_places=2, max_digits=3, default=0.00)
    commentCount = models.IntegerField(default=0)
    faceScore = models.DecimalField(decimal_places=2, max_digits=3, default=0.00)

    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title


class SearchQuery(models.Model):
    query = models.CharField(default='None', max_length=128)
    count = models.IntegerField(default=0)


    def __str__(self):
        return self.query

