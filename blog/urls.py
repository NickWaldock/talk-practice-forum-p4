from django.urls import path
from . import views


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('add-post/', views.AddPost.as_view(), name='add-post'),
    path('article/<int:pk>', views.PostView.as_view(), name='article'),
    path('article/update/<int:pk>', views.UpdatePost.as_view(), name='update-post'),
    path('article/delete-post/<int:pk>', views.DeletePost.as_view(), name='delete-post'),
    path('like/<int:pk>', views.LikeView, name='like_post'),
    path('add-category/', views.AddCategory.as_view(), name='add-category'),
    path('category/<str:category>/', views.Categories, name='category'),
    path('category-list/', views.CategoryList, name='category-list'),
]
