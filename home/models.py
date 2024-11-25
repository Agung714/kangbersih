
from django.db import models

class HomePage(models.Model):
    title = models.CharField(max_length=200)
    texttitle = models.CharField(max_length=200)
    SectionService = models.TextField()
    SectionServiceText = models.TextField()
    content = models.TextField()
    image = models.ImageField(upload_to='home/images/', blank=True, null=True)

    def __str__(self):
        return self.title
    

class ServiceHome(models.Model):
    nama_layanan = models.CharField(max_length=200)
    deskripsi = models.TextField()
    image = models.ImageField(upload_to='home/services/', blank=True, null=True)


    def __str__(self):
        return self.nama_layanan

        from django.db import models

class HomeImage(models.Model):
    image = models.ImageField(upload_to='home/section/')

    def __str__(self):
        return f"Image {self.id}"


class HomeItem(models.Model):
    item = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.item
        
class Testimoni(models.Model):
    nama = models.CharField(max_length=100, help_text="Nama pengirim testimoni")
    isi_testimoni = models.TextField(help_text="Isi testimoni")

    def __str__(self):
        return self.nama
