from django.urls import path

from apps.blog.views import PostCreateView, PostListView, LikePostView, CommentCreateView, LikedPostView


urlpatterns = [
    path('create/', PostCreateView.as_view(), name='post-create'),
    path('list/', PostListView.as_view(), name='post-list'),
    path('<int:post_id>/like/', LikePostView.as_view(), name='post-like'),
    path('<int:post_id>/unlike/', LikePostView.as_view(), name='post-unlike'),
    path('<int:post_id>/like/check/', LikedPostView.as_view(), name='post-liked'),
    path('<int:post_id>/comment/create/', CommentCreateView.as_view(), name='comment-create'),
]
