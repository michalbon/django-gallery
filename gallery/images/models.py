from django.db import models


class GalleryImage(models.Model):
    image = models.ImageField(upload_to='gallery_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

