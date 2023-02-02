from django.shortcuts import render

class NewsList(ListView):
    model = Post
    context_object_name = 'news'
    template_name = 'news.html'


class NewsDetail(DetailView):
    model = Post
    template_name = 'article.html'
    context_object_name = 'article'

