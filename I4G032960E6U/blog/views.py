from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from .models import Post
# Create your views here.


class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"


class PostCreateView(CreateView):
    model = Post
    fields = "__all__"
    template_name = "blog/post_form.html"


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"


class PostUpdateView(UpdateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")


class PostDeleteView(DeleteView):
    model = Post
    fields = "__all__"
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy("blog:all")
