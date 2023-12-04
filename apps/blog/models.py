from django.db import models
from apps.account.models import CustomUser


class Post(models.Model):
    shelter = models.ForeignKey(CustomUser, related_name='blog_posts', on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Like(models.Model):
    user = models.ForeignKey(CustomUser, related_name='post_likes', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)


class Comment(models.Model):
    user = models.ForeignKey(CustomUser, related_name='post_comments', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
