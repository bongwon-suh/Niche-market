from django.shortcuts import render
from django.views.generic import ListView,TemplateView
from post.models import Post
# Create your views here.

class PostList(ListView):
    model = Post
    template_name = 'post/post_list.html'
    context_object_name = 'posts'
