from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.urls import reverse


# STATUS = ((0, "Draft"), (1, "Published"))


# Database model for blog posts
class Post(models.Model):
    title = models.CharField(max_length=250, unique=True)
    # slug = models.SlugField(max_length=250, unique=True)
    subtitle = models.CharField(max_length=250, unique=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="blog_posts"
        )
    created_on = models.DateField(auto_now=True)
    updated_on = models.DateField(auto_now=True)
    body = models.TextField()
    tags = models.CharField(max_length=100)
    # featured_image = CloudinaryField('image', default='placeholder')
    # status = models.IntegerField(choices=STATUS, default=0)
    # likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home')

    # def number_of_likes(self):
    #     return self.likes.count()

    class Meta:
        ordering = ['-created_on']
        


# Database model for comments
# class Comment(models.Model):
#     post = models.ForeignKey(
#         Post,
#         on_delete=models.CASCADE,
#         related_name='comments'
#     )
#     username = models.CharField(max_length=40)
#     email = models.EmailField()
#     body = models.TextField()
#     date = models.DateTimeField(auto_now_add=True)
#     approved = models.BooleanField(default=False)

#     class Meta:
#         ordering = ['date']

#     def __str__(self):
#         return f"Comment {self.body} by {self.name}"

