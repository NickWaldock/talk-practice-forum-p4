from django.contrib import admin
from .models import Post, Category, Comment
from django_summernote.admin import SummernoteModelAdmin

admin.site.register(Category)


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'author', 'created_on', 'category')
    # list_display = ('title', 'author', 'slug', 'status', 'created_on')
    search_fields = ['title', 'subtitle', 'content']
    # prepopulated_fields = {'slug': ('title',)}
    list_filter = ('created_on', 'author')
    # list_filter = ('status', 'created_on')
    summernote_fields = ('body')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'username', 'body', 'date', 'approved')
    list_filter = ('approved', 'date')
    search_fields = ('username', 'email', 'body', 'post')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
