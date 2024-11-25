# services/views.py
from django.shortcuts import render
from .models import Layanan, ServicePage

# def services_view(request):
#     service_page = ServicePage.objects.prefetch_related('layanan').first()
#     return render(request, 'services/index.html', {'service_page': service_page})
 
#  experimen
def services_view(request):
    service_page = ServicePage.objects.prefetch_related('layanan').first()
    layanan = Layanan.objects.all()
    return render(request, 'services/index.html', {'service_page': service_page,'layanan': layanan})
