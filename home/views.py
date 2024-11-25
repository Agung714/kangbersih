from django.shortcuts import render
from django.shortcuts import render
from .models import HomePage, ServiceHome
from .models import HomeItem
from .models import HomeImage
from .models import Testimoni


def index(request):
    return render(request, "home/index.html")
# home/views.py

def home(request):
    content = HomePage.objects.first()
    services = ServiceHome.objects.all()
    items = HomeItem.objects.all()
    images = HomeImage.objects.all()[:3]  
    testimoni_list = Testimoni.objects.all()

    return render(request, 'home/index.html', {'content': content, 'services': services,'items': items,'images': images,'testimoni_list': testimoni_list})
    # return render(request, 'home.html', {'content': content, 'services': services})
 