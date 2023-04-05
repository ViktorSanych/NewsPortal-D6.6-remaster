from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post


class PostView(ListView):
    model = Post
    template_name = 'news/index.html'
    context_object_name = 'post'

    def get(self, request, *, object_list=None, **kwargs):
        news = Post.objects.all()
        context = {
            'news': news,
            'title': 'Список новостей'
        }
        return render(request, 'news/index.html', context)


class ViewPost(DetailView):
    model = Post
    context_object_name = 'post_item'
