# Generated by Django 5.1 on 2024-11-08 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maps_link', models.URLField(blank=True, max_length=500, null=True, verbose_name='Google Maps Link')),
                ('address', models.CharField(max_length=200, verbose_name='Alamat')),
                ('whatsapp_number', models.CharField(max_length=15, verbose_name='No WhatsApp')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Teks Tambahan')),
            ],
        ),
    ]
