from django.db import models

# Create your models here.

class Blog(models.Model):
    title_blog = models.CharField(max_length=30)
    date_blog = models.DateTimeField()
    text_blog = models.CharField(max_length=300)
    image_blog = models.ImageField(upload_to='event_images/')
