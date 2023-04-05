from django.urls import path
from .views import PostView, ViewPost

urlpatterns = [
    path('', PostView.as_view(), name='post_view'),
    path('<int:pk>/', ViewPost.as_view(), name='view_post'),   # было 'news/<int:pk>/', но так в адресе
    ]                                                                # получается news/news/, не красиво
