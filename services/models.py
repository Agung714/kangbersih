# services/models.py
from django.db import models

class ServicePage(models.Model):
    text = models.TextField()
    section_title = models.CharField(max_length=200)
    section_text = models.TextField()

    def __str__(self):
        return self.section_title

class Layanan(models.Model):
    service_page = models.ForeignKey(ServicePage, on_delete=models.CASCADE, related_name='layanan')
    nama_layanan = models.CharField(max_length=200)
    gambar = models.ImageField(upload_to='services/images/', blank=True, null=True)
    deskripsi_layanan = models.TextField()

    def __str__(self):
        return self.nama_layanan
 