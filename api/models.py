from django.db import models

# Create your models here.



class ImageMetadata(models.Model):
    image_url = models.URLField(max_length=200, unique=True)
    image_tags = models.CharField(max_length=2000)