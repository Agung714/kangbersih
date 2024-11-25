# blog/urls.py
from django.urls import path
from . import views
from .views import logout_view  # Impor view Anda


urlpatterns = [
    path('', views.blog_home, name='blog_home'),  # Halaman utama
    path('articles/', views.all_articles, name='all_articles'),  # Semua artikel
    path('article/<int:pk>/', views.article_detail, name='article_detail'),  # Detail artikel
    path('logout/', logout_view, name='custom_logout'),  
    path('article/<int:pk>/like/', views.like_article, name='like_article'),
]