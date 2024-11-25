from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='beranda'), 
    path('', views.home, name='beranda'), 
]
 
# urlpatterns = [
#     path('', views.about_view, name='about'),
# ]
 