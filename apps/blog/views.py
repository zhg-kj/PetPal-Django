from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Post, Like, Comment
from .serializers import PostSerializer, LikeSerializer, CommentSerializer


class PostCreateView(generics.CreateAPIView):
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        user = self.request.user
        if not user.is_seeker:
            serializer.save(shelter=user)
        else:
            return Response({'message': 'Seekers cannot create blog posts'}, status=status.HTTP_400_BAD_REQUEST)


class PostListView(generics.ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get_queryset(self):
        shelter_id = self.request.query_params.get('shelter_id')
        queryset = Post.objects.filter(shelter_id=shelter_id)
        return queryset.prefetch_related('comments')


class LikePostView(generics.GenericAPIView):
    serializer_class = LikeSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, post_id):
        post = generics.get_object_or_404(Post, pk=post_id)
        user = request.user
        liked = Like.objects.filter(post=post, user=user).exists()
        if not liked:
            Like.objects.create(post=post, user=user)
            return Response({'liked': True}, status=status.HTTP_201_CREATED)
        return Response({'message': 'You have already liked this post'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, post_id):
        post = generics.get_object_or_404(Post, pk=post_id)
        user = request.user
        like = Like.objects.filter(post=post, user=user)
        if like.exists():
            like.delete()
            return Response({'message': 'Like removed'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'message': 'You have not liked this post'}, status=status.HTTP_400_BAD_REQUEST)


class LikedPostView(generics.GenericAPIView):
    serializer_class = LikeSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, post_id):
        post = generics.get_object_or_404(Post, pk=post_id)
        user = request.user
        liked = Like.objects.filter(post=post, user=user).exists()
        return Response({'liked': liked})


class CommentCreateView(generics.CreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        post_id = self.kwargs['post_id']
        post = generics.get_object_or_404(Post, pk=post_id)
        serializer.save(user=self.request.user, post=post)
