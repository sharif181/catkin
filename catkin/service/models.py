from django.db import models


class Feature(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    

def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)

class Technology(models.Model):
    title = models.CharField(max_length=255)
    image_url = models.ImageField(upload_to=upload_to)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=255)
    feature = models.ManyToManyField(Feature, blank=True, null=True)


    def __str__(self):
        return self.title


class Service(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    technologies = models.ManyToManyField(Technology)
    catagories = models.ManyToManyField(Category)
    features = models.ManyToManyField(Feature)


    def __str__(self):
        return self.title
