from rest_framework import generics
from rest_framework.permissions import *
from post.models import Post as PostModel
from post.api.serializers import (
    PostListSerializer,
    PostRetrieveSerializer,
)

class PostListView(generics.ListAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostListSerializer


class PostRetrieveView(generics.RetrieveAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostRetrieveSerializer
        permission_classes = (AllowAny,)