from django.http import Http404
from rest_framework import viewsets, status
from rest_framework.exceptions import PermissionDenied
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import LimitOffsetPagination

from rest_framework.response import Response
from .permissions import IsAdminOrOwner, IsAuthenticatedOrReadonly
from .models import News, Like, Comment
from .serializers import NewsSerializer, CommentSerializer


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [IsAuthenticatedOrReadonly, IsAdminOrOwner]

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.prefetch_related(
            "comments"
        )  # Prefetch related comments to reduce database queries
        return queryset

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        instance = serializer.save()
        if instance.author != self.request.user:
            raise PermissionDenied(
                "You do not have permission to update this news article."
            )

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise PermissionDenied(
                "You do not have permission to delete this news article."
            )
        instance.delete()


class CommentAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadonly]

    def get(self, request, news_id):
        comments = Comment.objects.filter(news__id=news_id)
        paginator = LimitOffsetPagination()
        paginated_comments = paginator.paginate_queryset(comments, request)
        serializer = CommentSerializer(paginated_comments, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, news_id):
        data = request.data.copy()
        print(request, news_id)
        data["news"] = news_id
        serializer = CommentSerializer(data=data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, news_id, comment_id):
        try:
            comment = Comment.objects.get(pk=comment_id, news__id=news_id)
            if (
                not request.user.role == "admin"
                or request.user.id != comment.author.id
                or request.user.id != comment.news.author.id
            ):
                raise PermissionDenied(
                    "You do not have permission to delete this news article."
                )
            self.check_object_permissions(request, comment)
            comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Comment.DoesNotExist:
            raise Http404


class LikeNewsAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, news_id):
        news = News.objects.get(pk=news_id)
        user = request.user

        # Проверка, есть ли уже лайк пользователя под этой новостью
        try:
            like = Like.objects.get(news=news, user=user)
            # Лайк уже существует, удаляем его
            like.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Like.DoesNotExist:
            # Лайк не существует, создаем новый лайк
            Like.objects.create(news=news, user=user)
            return Response(status=status.HTTP_201_CREATED)
