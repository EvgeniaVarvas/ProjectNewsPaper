from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .filters import PostFilter
from .forms import PostForm
from .models import Author, Post



class PostListMixin:
    model = Post
    post_type_filter = None
    paginate_by = 10


    def get_queryset(self):
        return Post.objects.filter(post_type=self.post_type_filter).order_by('-created')
 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news'] = context['object_list']  
        return context
    
class NewsList(PostListMixin, ListView):
    post_type_filter = 'news'
    template_name = 'common_list.html'

class ArticleList(PostListMixin, ListView):
    post_type_filter = 'article'
    template_name = 'common_list.html' 

class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post_detail'   

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news'] = context['object']
        return context    


class AuthorMixin:
    def form_valid(self, form):
        author_instance, created = Author.objects.get_or_create(user=self.request.user)
        form.instance.author = author_instance
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.pk})
    
class PostCreate(AuthorMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'create_news.html'

class PostUpdate(AuthorMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'create_news.html'    
    

class PostDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('news_list')

class PostSearch(ListView):
    model = Post
    context_object_name = 'post_search'
    template_name = 'post_search.html'


    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context     

      