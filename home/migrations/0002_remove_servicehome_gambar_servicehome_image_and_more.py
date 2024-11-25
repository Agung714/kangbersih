# Generated by Django 5.1 on 2024-11-08 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicehome',
            name='gambar',
        ),
        migrations.AddField(
            model_name='servicehome',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='home/services/'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='home/images/'),
        ),
    ]