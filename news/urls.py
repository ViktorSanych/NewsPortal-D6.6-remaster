from django.urls import path
from .views import PostView, ViewPost

urlpatterns = [
    path('', PostView.as_view(), name='post_view'),
    path('page/<int:page_number>', PostView.as_view(), name='paginator'),
    path('news/<int:pk>/', ViewPost.as_view(), name='view_post'),
    ]
