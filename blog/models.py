from django.db import models

# Create your models here.

class Blog(request):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    body = models.TextField()
    posted = models.DateTimeField(db_index=True, auto_now_add=True)
    