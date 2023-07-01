from rest_framework import serializers
from .models import News, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "news", "text", "author", "date"]
        read_only_fields = ["id", "author", "date"]


class NewsSerializer(serializers.ModelSerializer):
    latest_10_comments = serializers.SerializerMethodField()
    like_count = serializers.SerializerMethodField()
    comment_count = serializers.SerializerMethodField()

    def get_latest_10_comments(self, news):
        comments = Comment.objects.filter(news=news).order_by("-date")[:10]
        serializer = CommentSerializer(comments, many=True)
        return serializer.data

    def get_like_count(self, news):
        return news.like_set.count()

    def get_comment_count(self, news):
        return news.comments.count()

    class Meta:
        model = News
        fields = [
            "id",
            "title",
            "text",
            "author",
            "date",
            "like_count",
            "comment_count",
            "latest_10_comments",
        ]
        read_only_fields = [
            "id",
            "author",
            "date",
            "like_count",
            "comment_count",
            "latest_10_comments",
        ]
