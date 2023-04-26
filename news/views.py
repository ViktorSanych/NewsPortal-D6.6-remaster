from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.core.paginator import Paginator

from .models import Post


class PostView(ListView):
    model = Post
    template_name = 'news/news.html'
    context_object_name = 'posts'
    paginate_by = 2

    def get(self, request, object_list=None, **kwargs):
        news = Post.objects.all()
        context = {
            'news': news,
            'title': 'Список новостей'
        }
        return render(request, 'news/news.html', context)


class ViewPost(DetailView):
    model = Post
    context_object_name = 'post'
