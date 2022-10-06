from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import About, Post
from django.contrib.auth.models import User


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_post.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView): # <app>/<model>_<viewtype>.html
    model = Post
    
class PostCreateView(LoginRequiredMixin ,CreateView): # <app>/<model>_<viewtype>.html
    model = Post
    fields = ['title', 'content']

    # ghi đè user hien tai cho filed author trong model Post 
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin ,UpdateView): # <app>/<model>_<viewtype>.html
    model = Post
    fields = ['title', 'content']

    # ghi đè user hien tai cho filed author trong model Post 
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView): # <app>/<model>_<viewtype>.html
    model = Post
    success_url = '/'
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
def aboutView(request):
    content = About.objects.first().content
    return render(request, 'blog/about.html', {'content': content})
    