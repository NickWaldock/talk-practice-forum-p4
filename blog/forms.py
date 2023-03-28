from django import forms
from .models import Post, Category, Comment


# Create a dynamic list of category items for use in PostForm
# and Update form models
categories = Category.objects.all().values_list('name', 'name')
category_list = []
for item in categories:
    category_list.append(item)


# Form for creating new posts
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'subtitle', 'category', 'author', 'body', 'tags')

        widgets = {  # For bootstrap form styling
            'title': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Write a concise title...'
                       }),
            'subtitle': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Add a bit more context...'
                       }),
            'author': forms.TextInput(
                attrs={'class': 'form-control',
                       'value': '',
                       'id': 'authorField',
                       'type': 'hidden'
                       }),
            'category': forms.Select(
                choices=category_list,
                attrs={'class': 'form-control',
                       }),
            'body': forms.Textarea(
                attrs={'class': 'form-control',
                       'placeholder': 'What do you want to share?'
                       }),
            'tags': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Add any relevant tags here!'
                       }),
        }


# Form for updating posts
class UpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'subtitle', 'body', 'tags')

        widgets = {  # For bootstrap form styling
            'title': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Write a concise title...'
                       }),
            'subtitle': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Add a bit more context...'
                       }),
            'body': forms.Textarea(
                attrs={'class': 'form-control',
                       'placeholder': 'What do you want to share?'
                       }),
            'tags': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Add any relevant tags here!'
                       }),
        }


# Form for creating and submitting comments on posts
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        widgets = {
            'body': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Write your comment here...'
                       })
        }
        labels = {'body': ''}
