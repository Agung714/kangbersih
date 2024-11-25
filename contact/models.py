from django.db import models

class ContactInfo(models.Model):
    maps_link = models.URLField("Google Maps Link", max_length=500, blank=True, null=True)
    address = models.CharField("Alamat", max_length=200)
    whatsapp_number = models.CharField("No WhatsApp", max_length=15)
    email = models.EmailField("Email")
    description = models.TextField("Teks Tambahan", blank=True, null=True)

    def __str__(self):
        return self.address
