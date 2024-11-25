from django.shortcuts import render
from .models import ContactInfo

def contact_view(request):
    contact_info = ContactInfo.objects.first()  # Ambil data pertama
    return render(request, 'contact/index.html', {'contact_info': contact_info})
