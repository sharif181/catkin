from django.db import models

def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)

class ClientReview(models.Model):
    client_name = models.CharField(max_length=255)
    client_image = models.ImageField(upload_to=upload_to, blank=True, null=True)
    country_image = models.ImageField(upload_to=upload_to, blank=True, null=True)
    review_content = models.TextField()


    def __str__(self):
        return f'{self.client_name}'
