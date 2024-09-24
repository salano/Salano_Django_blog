from django.shortcuts import render
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


# overriding defaults
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']


# using defaults
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html' #cannot use override since I am using salano_blog
 

# using defaults
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title','content']
    template_name = 'blog/post_form.html' #cannot use override since I am using salano_blog

    def form_valid(self, form):
        # Set form user to currently logged in user
        form.instance.author = self.request.user
        return super().form_valid(form)


# using defaults
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title','content']
    template_name = 'blog/post_form.html' #cannot use override since I am using salano_blog

    def form_valid(self, form):
        # Set form user to currently logged in user
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    # test to enable update check
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    

# using defaults
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    template_name = 'blog/post_confirm_delete.html' # cannot use override since I am using salano_blog
    
    # test to enable update check
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
