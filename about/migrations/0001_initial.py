# Generated by Django 5.1 on 2024-11-08 02:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('StrukturUsaha', models.TextField()),
                ('visi', models.TextField()),
                ('title_section', models.CharField(max_length=200)),
                ('teks_section', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='AboutImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='about/images/')),
                ('about_page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='about.aboutpage')),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gambar', models.ImageField(blank=True, null=True, upload_to='about/cards/')),
                ('nama', models.CharField(max_length=200)),
                ('deskripsi', models.TextField()),
                ('about_page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cards', to='about.aboutpage')),
            ],
        ),
        migrations.CreateModel(
            name='Misi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teks', models.TextField()),
                ('about_page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='misi', to='about.aboutpage')),
            ],
        ),
    ]
