from django.db import models
from service.models import Technology


def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)


class ProjectImage(models.Model):
    project_title = models.CharField(max_length=255)
    image_url = models.ImageField(upload_to=upload_to)
    

    def __str__(self):
        return self.project_title



class Project(models.Model):
    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    live_preview_link = models.CharField(max_length=255, blank=True, null=True)
    video_url = models.CharField(max_length=255, blank=True, null=True)
    technologies = models.ManyToManyField(Technology, blank=True, null=True)
    images = models.ManyToManyField(ProjectImage)


    def __str__(self):
        return self.title


