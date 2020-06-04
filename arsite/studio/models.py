from django.db import models
from library.models import Video


class MultipleChoiceQuiz(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    prompt = models.TextField()
    timestamp = models.IntegerField(default=0)

    option1 = models.TextField()
    option2 = models.TextField()
    option3 = models.TextField()
    option4 = models.TextField()
    key = models.IntegerField()  # an int between 1-4

    option1_redirect = models.URLField()
    option2_redirect = models.URLField()
    option3_redirect = models.URLField()
    option4_redirect = models.URLField()

    def __str__(self):
        return f"{video}: {prompt}"
