from django.db import models

# class Video(models.Model):

#     TAGS = [
#         ('NEW', 'New'),
#         ('CRE', 'Credible'),
#         ('INT', 'Interactive'),
#         ('PER', 'Personal'),
#         ('ANI', 'Animated'),
#         ('P&P', 'Paper & Pencil'),
#     ]

#     title = models.CharField(max_length=128)
#     url = models.URLField(max_length=256, default='None')
#     thumbnail = models.URLField(max_length=256, default='None')
#     author = models.CharField(max_length=64)
#     date = models.DateField()
#     description = models.TextField()
#     length = models.IntegerField()
#     views = models.IntegerField()
#     rating = models.DecimalField(decimal_places=2, max_digits=3, default=0.00)
#     tag1 = models.CharField(max_length=3, choices=TAGS, default='None')
#     tag2 = models.CharField(max_length=3, choices=TAGS, default='None')
#     tag3 = models.CharField(max_length=3, choices=TAGS, default='None')
    