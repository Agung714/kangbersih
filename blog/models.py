# blog/models.py
from django.db import models
from django.contrib.auth.models import User  # User OAuth2 otomatis kompatibel


class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='articles/')
    created_at = models.DateTimeField(auto_now_add=True)
    # likes = models.PositiveIntegerField(default=0)
    likes = models.ManyToManyField(User, related_name='liked_articles', blank=True)


    # comments_count = models.PositiveIntegerField(default=0)
    def likes_count(self):
        return self.likes.count()

    def __str__(self):
        return self.title



class Comment(models.Model):
    article = models.ForeignKey(Article, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Referensi ke pengguna login
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.article.title}'
