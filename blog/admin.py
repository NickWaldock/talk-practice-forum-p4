from django.contrib import admin
from .models import Post, Category, Comment, Contact
from django_summernote.admin import SummernoteModelAdmin

admin.site.register(Category)


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'author', 'created_on', 'category')
    search_fields = ['title', 'subtitle', 'content']
    list_filter = ('created_on', 'author')
    summernote_fields = ('body')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'username', 'body', 'date', 'approved')
    list_filter = ('approved', 'date')
    search_fields = ('username', 'email', 'body', 'post')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'member', 'date')
    list_filter = ('date', 'name', 'member')
    search_fields = ['name', 'subject']
    summernote_fields = ('message')
