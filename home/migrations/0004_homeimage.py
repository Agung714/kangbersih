# Generated by Django 5.1 on 2024-11-12 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_homeitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='home/section/')),
            ],
        ),
    ]
