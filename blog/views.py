from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from .models import Post, Category, Comment
from .forms import PostForm, UpdateForm, CommentForm


# View to list all posts
class PostList(generic.ListView):
    model = Post
    # queryset = Post.objects.filter(status=1).order_by('-created_on')
    queryset = Post.objects.order_by('-created_on')
    template_name = 'index.html'
    # paginate_by = 10

    # Context for the dynamic categories nav links
    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(PostList, self).get_context_data(*args, **kwargs)
        context["category_menu"] = category_menu
        return context


# Display a single post in a single page
class PostView(generic.DetailView):
    model = Post
    template_name = 'article.html'
    form_class = CommentForm

    # Context for the dynamic categories nav links, likes, and comments
    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(PostView, self).get_context_data(*args, **kwargs)
        likes_count = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = likes_count.number_of_likes()
        liked = False
        if likes_count.likes.filter(id=self.request.user.id).exists():
            liked = True
        context["form"] = CommentForm()
        context["category_menu"] = category_menu
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.username = request.user
            comment.post_id = self.get_object().id
            comment.save()
            return redirect('article', self.get_object().id)


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
    

# Displays a list of all the categories
def CategoryList(request):
    category_menu_list = Category.objects.all()
    return render(request, 'category-list.html', {'category_menu_list': category_menu_list})


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
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('article', args=[str(pk)]))


# View for adding comments
class AddComment(generic.CreateView):
    model = Comment
    # form_class = CommentForm
    template_name = 'add-comment.html'
    fields = '__all__'