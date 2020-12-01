from django.db import models

# Create your models here.

class Blog(models.Model):
    title_blog = models.CharField(max_length=30)
    date_blog = models.DateTimeField()
    text_blog = models.TextField()
    image_blog = models.ImageField(upload_to='event_images/')

    def get_summary(self):
        return self.text_blog[:70]

    def __str__(self):
        return self.title_blog
