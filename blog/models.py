from django.db import models
from portfolio.util import unique_slug_generator
from django.utils.text import slugify 
from django.db.models.signals import pre_save
from django.db.models.signals import post_save


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=250, db_index=True)
    slug = models.SlugField(max_length=250, db_index=True)
    body = models.TextField()
    posted = models.DateTimeField(db_index=True, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
      
    def __str__(self): 
       return self.title 

def pre_save_receiver(sender, instance, *args, **kwargs): 
        if not instance.slug:
            instance.slug = unique_slug_generator(instance) 

pre_save.connect(pre_save_receiver, sender = Post) 
