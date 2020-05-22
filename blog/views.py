from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.http import HttpResponse
from .models import Post

def about(request):
    return render(request, 'blog/about.html')

#function call to render plot data
def show_plot(request):
    return render(request, 'blog/plot.html')

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context) #render returns http response

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5 #number of posts per page

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username')) #get username from url
        return Post.objects.filter(author=user).order_by('-date_posted')
    

class PostDetailView(DetailView):
    model = Post
    
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user #before submission ensure the author is set
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user #before submission ensure the author is set
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object() #get the post we are updating
        if self.request.user == post.author:
            return True
        return False #I hate this conditional

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object() #get the post we are updating
        if self.request.user == post.author:
            return True
        return False #I hate this conditional


def about(request):
    return render(request, 'blog/about.html', {'title': 'about'})



#class-based views have more built in functionality
#list views, detail views, etc...  