from django.shortcuts import render
from django.views import generic
from .models import Post, Comment


# View to list all posts
class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    # paginate_by = 10


# View to view a single post in a single page
class PostView(generic.DetailView):
    model = Post
    template_name = 'article.html'


# View to add a post
class AddPost(generic.CreateView):
    model = Post
    template_name = 'add-post.html'
    slug_field = 'slug'
    # fields = '__all__'
    fields = ('title', 'author', 'subtitle', 'body', 'tags')

    def get_object(self):
        slug = self.kwargs.get("slug")
        return get_object_or_404(Post, slug=slug)
