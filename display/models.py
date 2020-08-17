from django.db import models

# Create your models here.

class Profile(models.Model):
    image = models.ImageField(upload_to='image/')
    title = models.CharField(max_length=200, default = 'New Title')
