from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'subtitle', 'author', 'body', 'tags')

        widgets = {  # For bootstrap form styling
            'title': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Write a concise title...'
                       }),
            'subtitle': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Add a bit more context...'
                       }),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(
                attrs={'class': 'form-control',
                       'placeholder': 'What do you want to share?'
                       }),
            'tags': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Add any relevant tags here!'
                       }),
        }


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