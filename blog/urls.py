from django.urls import path
from .views import (
    PostListView, PostDetailView, 
    PostCreateView, PostUpdateView,
    PostDeleteView, UserPostListView)
from . import views

import blog.dash_app


urlpatterns = [
    #convert class view into actual view object
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    #create route from primary key of post (pk)
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('plot/', views.show_plot, name='sample-plot'),
    path('about/', views.about, name='about-me'),
]
