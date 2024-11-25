# gallery/models.py
from django.db import models

class GalleryImage(models.Model):
    image = models.ImageField(upload_to='gallery/images/')
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Gambar diupload pada {self.upload_date.strftime('%Y-%m-%d %H:%M:%S')}"

