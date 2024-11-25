# about/admin.py
from django.contrib import admin
from .models import AboutPage, Misi, Card, AboutImage

class MisiInline(admin.TabularInline):
    model = Misi
    extra = 1

class CardInline(admin.TabularInline):
    model = Card
    extra = 1

class AboutImageInline(admin.TabularInline):
    model = AboutImage
    extra = 1

class AboutPageAdmin(admin.ModelAdmin):
    inlines = [MisiInline, CardInline, AboutImageInline]

admin.site.register(AboutPage, AboutPageAdmin)
