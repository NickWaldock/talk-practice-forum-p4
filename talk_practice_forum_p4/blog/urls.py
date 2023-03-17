from django.urls import path
from . import views


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('add-post/', views.AddPost.as_view(), name='add-post'),
]