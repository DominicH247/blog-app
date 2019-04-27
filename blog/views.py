from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy 

from .models import Post

class BlogListView(ListView):
	"""class based view home page displaying posts"""
	model = Post
	template_name = 'blog/home.html'


class BlogDetailView(DetailView):
	"""class based view for individual blog posts"""
	model = Post
	template_name = 'blog/post_detail.html'

class BlogCreateView(CreateView):
	"""class based view for creation of new blog posts form page"""
	model = Post
	template_name = 'blog/post_new.html'
	fields = ['title', 'author', 'body']


class BlogUpdateView(UpdateView):
	"""class based update post view"""
	model = Post
	template_name = 'blog/post_edit.html'
	fields = ['title', 'body']


class BlogDeleteView(DeleteView):
	""" class based view post delete"""
	model = Post
	template_name = 'blog/post_delete.html'
	success_url = reverse_lazy('home')








