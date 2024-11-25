from django.contrib import admin

# Register your models here.
 # blog/admin.py
from django.contrib import admin
from .models import Article, Comment

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1  # Menambahkan form komentar di halaman artikel

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'content')
    list_filter = ('created_at',)
    inlines = [CommentInline]  # Menampilkan komentar terkait di halaman artikel

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
