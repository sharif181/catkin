from django.db import models

class ContactUs(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.email}"
    
    class Meta:
        verbose_name_plural = "contact us"
