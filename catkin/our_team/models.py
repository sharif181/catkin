from django.db import models


class Designation(models.Model):
    title = models.CharField(max_length=255)
    short_form = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        return f'{self.title} - {self.short_form}'

def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)

class TeamMember(models.Model):
    name = models.CharField(max_length=255)
    employee_id = models.CharField(max_length=100)
    designation = models.ForeignKey(Designation, on_delete=models.DO_NOTHING)
    linked_in_link = models.CharField(max_length=255, blank=True, null=True)
    profile_link = models.CharField(max_length=255, blank=True, null=True)
    image_url = models.ImageField(upload_to=upload_to)

    def __str__(self):
        return f'{self.name} - {self.designation.title}'

