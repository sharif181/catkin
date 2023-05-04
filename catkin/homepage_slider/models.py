from django.db import models

class HomePageSlider(models.Model):
    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f"{self.title}"
    
