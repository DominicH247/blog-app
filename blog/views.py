from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

class BlogListView(ListView):
	"""class based view home page displaying posts"""
	model = Post
	template_name = 'blog/home.html'

class BlogDetailView(DetailView):
	"""class based view for individual blog posts"""
	model = Post
	template_name = 'blog/post_detail.html'
