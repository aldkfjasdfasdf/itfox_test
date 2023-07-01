from django.urls import path
from rest_framework import routers
from .views import NewsViewSet, CommentAPIView, LikeNewsAPIView

router = routers.DefaultRouter()
router.register(r"news", NewsViewSet)
urlpatterns = [
    path("comments/<int:news_id>/", CommentAPIView.as_view(), name="comment"),
    path(
        "comments/<int:news_id>/<int:comment_id>/",
        CommentAPIView.as_view(),
        name="comment-detail",
    ),
    path("like/<int:news_id>/", LikeNewsAPIView.as_view(), name="like-news"),
]
urlpatterns += router.urls
