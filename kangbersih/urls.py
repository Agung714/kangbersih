"""
URL configuration for kangbersih project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('social_django.urls', namespace='social')),
    
    # path('accounts/', include('allauth.urls')),  # This includes allauth URLs for login/logout
    path('logout/', LogoutView.as_view(), name='logout'),  # Tambahkan ini
    path('', include('home.urls')),
    path('gallery/', include('gallery.urls')),  # Tambahkan URL untuk galeri
    path('about/', include('about.urls')),  # URL untuk halaman about
    path('blog/', include('blog.urls')),  # Tambahkan rute ke halaman Blog
    path('contact/', include('contact.urls')),  # URL untuk contact
    path('services/', include('services.urls')),
    # path('auth/', include('social_django.urls', namespace='social')),
]

 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 