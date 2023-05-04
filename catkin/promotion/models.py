from django.db import models

class Promotion(models.Model):
    title = models.CharField(max_length=255)
    desciption = models.TextField()
    video_link = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.title}'
