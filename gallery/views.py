# gallery/views.py
from django.shortcuts import render
from .models import GalleryImage
from django.core.paginator import Paginator

def gallery_view(request):
    images = GalleryImage.objects.all().order_by('-upload_date')
    paginator = Paginator(images, 6)  # Show 6 images per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'gallery/index.html', {'page_obj': page_obj})

    # return render(request, 'gallery/index.html', {'images': images})
