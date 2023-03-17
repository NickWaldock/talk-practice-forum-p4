from django.shortcuts import render
from django.views import generic
from .models import Post, Comment


# View to list all posts
class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 10


# View to add a post
class AddPost(generic.CreateView):
    model = Post
    template_name = 'add-post.html'
    fields = '__all__'
