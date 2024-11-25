# services/admin.py
from django.contrib import admin
from .models import ServicePage, Layanan

class LayananInline(admin.TabularInline):
    model = Layanan
    extra = 1

@admin.register(ServicePage)
class ServicePageAdmin(admin.ModelAdmin):
    inlines = [LayananInline]
    list_display = ['section_title']
