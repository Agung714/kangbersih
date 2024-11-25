# about/models.py
from django.db import models
 
class AboutPage(models.Model):
    title = models.CharField(max_length=200)
    StrukturUsaha = models.TextField()
    visi = models.TextField()
    title_section = models.CharField(max_length=200)
    teks_section = models.TextField()

    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.title
class Misi(models.Model):
    about_page = models.ForeignKey(AboutPage, on_delete=models.CASCADE, related_name='misi')
    teks = models.TextField()

    def __str__(self):
        return self.teks[:50]  # Menampilkan potongan teks misi

class Card(models.Model):
    about_page = models.ForeignKey(AboutPage, on_delete=models.CASCADE, related_name='cards')
    gambar = models.ImageField(upload_to='about/cards/', blank=True, null=True)
    nama = models.CharField(max_length=200)
    deskripsi = models.TextField()

    def __str__(self):
        return self.nama
class AboutImage(models.Model):
    about_page = models.ForeignKey(AboutPage, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='about/images/')

    def __str__(self):
        return f"Gambar untuk {self.about_page.title}"

