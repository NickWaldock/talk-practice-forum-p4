from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from .models import Post, Category
from .forms import PostForm, UpdateForm


# View to list all posts
class PostList(generic.ListView):
    model = Post
    # queryset = Post.objects.filter(status=1).order_by('-created_on')
    queryset = Post.objects.order_by('-created_on')
    template_name = 'index.html'
    # paginate_by = 10


# View to view a single post in a single page
class PostView(generic.DetailView):
    model = Post
    template_name = 'article.html'

    # def get_context_data(self, *args, **kwargs):
    #     context = super(PostView, self)


# View to add a post
class AddPost(generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add-post.html'
    slug_field = 'slug'

    # def get_object(self):
    #     slug = self.kwargs.get("slug")
    #     return get_object_or_404(Post, slug=slug)


# View to update a post
class UpdatePost(generic.UpdateView):
    model = Post
    form_class = UpdateForm
    template_name = 'update-post.html'


# View to delete a post
class DeletePost(generic.DeleteView):
    model = Post
    template_name = 'delete-post.html'
    success_url = reverse_lazy('home')


# View for creating new categories
class AddCategory(generic.CreateView):
    model = Category
    template_name = 'add-category.html'
    fields = '__all__'
    


# View for displaying all posts within a certain category
def Categories(request, category):
    category_posts = Post.objects.filter(category=category)
    return render(request, 'categories.html',
                  {'category': category,
                   'category_posts': category_posts}
                  )


# View for likes
def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('article', args=[str(pk)]))
