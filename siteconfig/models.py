from django.db import models

class ContactInfo(models.Model):
    whatsapp_number = models.CharField(
        max_length=15, 
        help_text="Masukkan nomor WhatsApp dalam format internasional, misalnya: +628123456789"
    )

    def __str__(self):
        return self.whatsapp_number
