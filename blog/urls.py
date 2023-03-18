from django.urls import path
from . import views


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('add-post/', views.AddPost.as_view(), name='add-post'),
    path('article/<int:pk>', views.PostView.as_view(), name='article'),
]
