from django.urls import path
from post.api.views import(
    PostListView,
    PostRetrieveView,
)


app_name = 'post'
urlpatterns = [
    path('', PostListView.as_view(), name='list_post'),
    path('<pk>', PostRetrieveView.as_view(), name='post_detail'),

    # re_path
]
