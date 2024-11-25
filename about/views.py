
# about/views.py
from django.shortcuts import render
from .models import AboutPage
 
# pke ini nnti
def about_view(request):
    # about_page = AboutPage.objects.first()
    about_page = AboutPage.objects.prefetch_related('misi', 'cards', 'images').first()
    
    return render(request, 'about/index.html', {'about_page': about_page})
# def about_view(request):
#     return render(request, 'about/index.html')
