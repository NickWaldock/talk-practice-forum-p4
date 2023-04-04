from django import forms
from .models import Post, Category, Comment, Contact


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
        fields = ('title', 'subtitle', 'category', 'author', 'body')
        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-field',
                       'placeholder': 'Write a concise title...'
                       }),
            'subtitle': forms.TextInput(
                attrs={'class': 'form-field',
                       'placeholder': 'Add a bit more context...'
                       }),
            'author': forms.TextInput(
                attrs={'value': '',
                       'id': 'authorField',
                       'type': 'hidden'
                       }),
            'category': forms.Select(
                choices=category_list,
                attrs={'class': 'form-field',
                       }),
            'body': forms.Textarea(
                attrs={'class': 'form-field',
                       'placeholder': 'What do you want to share?'
                       }),
        }
        labels = {
            'title': '',
            'subtitle': '',
            'category': 'Choose a category...',
            'body': '',
        }


# Form for updating posts
class UpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'subtitle', 'body')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-field'}),
            'subtitle': forms.TextInput(attrs={'class': 'form-field'}),
            'body': forms.Textarea(attrs={'class': 'form-field'}),
        }


# Form for creating and submitting comments on posts
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        widgets = {
            'body': forms.TextInput(
                attrs={'class': 'form-field',
                       'placeholder': 'Write your comment here...'
                       })
        }
        labels = {'body': ''}


# Contact Form
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = 'name', 'email', 'subject', 'message', 'member'
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-field',
                       'placeholder': 'Name'
                       }),
            'email': forms.EmailInput(
                attrs={'class': 'form-field',
                       'placeholder': 'Email'
                       }),
            'subject': forms.TextInput(
                attrs={'class': 'form-field',
                       'placeholder': 'What is your message about?'
                       }),
            'message': forms.Textarea(
                attrs={'class': 'form-field',
                       'placeholder': 'Write your message here...'
                       }),
            'member': forms.CheckboxInput()
        }
        labels = {
            'name': '',
            'email': '',
            'subject': '',
            'message': '',
            'member': ''
        }
