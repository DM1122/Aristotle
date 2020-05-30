from django.db import models



class Tag(models.Model):
    name = models.CharField(max_length=16)

    def __str__(self):
        return self.name


class Video(models.Model):
    title = models.CharField(max_length=128)
    url = models.URLField(max_length=256, default='')
    thumbnail = models.URLField(max_length=256, default='')
    author = models.CharField(max_length=64)
    date = models.DateField()
    description = models.TextField()
    duration = models.IntegerField()
    views = models.IntegerField()
    rating = models.DecimalField(decimal_places=2, max_digits=3, default=0.00)
    face_score = models.DecimalField(decimal_places=2, max_digits=3, default=0.00)

    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title


