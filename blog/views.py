from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, Comment
from django.contrib.auth import logout
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Count

def blog_home(request):
    # latest_articles = Article.objects.all().order_by('-created_at')[:6]  # 5 artikel terbaru
    # favorite_articles = Article.objects.all().order_by('-likes')[:6]     # 5 artikel terfavorit
    # popular_articles = Article.objects.all().order_by('-comments_count')[:6]  # 5 artikel teramai
    latest_articles = Article.objects.annotate(
        comments_count=Count('comments'),
        likes_count=Count('likes')  # Jika Anda menggunakan ManyToManyField untuk likes
    ).order_by('-created_at')[:6]
    favorite_articles = Article.objects.annotate(
        comments_count=Count('comments'),
        likes_count=Count('likes')
    ).order_by('-likes_count')[:6]

    popular_articles = Article.objects.annotate(
        comments_count=Count('comments'),
        likes_count=Count('likes')
    ).order_by('-comments_count')[:6]

    context = {
        'latest_articles': latest_articles,
        'favorite_articles': favorite_articles,
        'popular_articles': popular_articles
    }
    return render(request, 'blog/index.html', context)

from django.shortcuts import render
from .models import Article


from django.core.paginator import Paginator

def all_articles(request):
    query = request.GET.get('search', '')  # Ambil parameter pencarian dari URL
    if query:
        articles = Article.objects.filter(title__icontains=query)  # Filter berdasarkan judul
    else:
        articles = Article.objects.all()  # Tampilkan semua artikel jika tidak ada pencarian

    # Tambahkan pagination
    # paginator = Paginator(articles, 6)  # 6 artikel per halaman
    paginator = Paginator(articles.annotate(comments_count=Count('comments')), 6)  # 6 artikel per halaman
    page_number = request.GET.get('page')  # Ambil nomor halaman dari parameter URL
    page_obj = paginator.get_page(page_number)  # Dapatkan objek halaman

    context = {
        'articles': page_obj,  # Ganti dengan objek halaman
        'query': query,        # Kirimkan pencarian agar tetap ada di template
    }
    return render(request, 'blog/all.html', context)



# @login_required
def article_detail(request, pk):
    # article = get_object_or_404(Article, pk=pk)
    article = get_object_or_404(
        Article.objects.annotate(comments_count=Count('comments')),
        pk=pk
    )

    comments = article.comments.all()

    if request.method == "POST":
        # Mengambil konten komentar dari form
        content = request.POST.get('content')

        # Membuat komentar baru dengan pengguna yang sedang login
        Comment.objects.create(
            article=article,
            user=request.user,  # Referensi ke pengguna yang login
            content=content
        )

        # Perbarui jumlah komentar artikel
        article.comments_count += 1
        article.save()

        # Redirect untuk menghindari pengiriman ulang form
        return redirect('article_detail', pk=article.pk)

    context = {
        'article': article,
        'comments': comments
    }
    return render(request, 'blog/read.html', context)


# app_blog/views.py


def logout_view(request):
    """Custom logout view that logs the user out and redirects to Google logout."""
    logout(request)  # Hapus sesi user
    return redirect("https://accounts.google.com/Logout?continue=/accounts/login/")  # Redirect ke Google logout


def like_article(request, pk):
    if request.method == 'POST' and request.user.is_authenticated:
        article = get_object_or_404(Article, pk=pk)
        if request.user in article.likes.all():
            article.likes.remove(request.user)
            liked = False
        else:
            article.likes.add(request.user)
            liked = True
        return JsonResponse({'liked': liked, 'like_count': article.likes.count()})
    return JsonResponse({'error': 'Invalid request'}, status=400)



# def all_articles(request):
#     query = request.GET.get('search', '')  # Ambil parameter pencarian dari URL
#     if query:
#         articles = Article.objects.filter(title__icontains=query)  # Filter berdasarkan judul
#     else:
#         articles = Article.objects.all()  # Tampilkan semua artikel jika tidak ada pencarian

#     context = {
#         'articles': articles,
#     }
#     return render(request, 'blog/all.html', context)