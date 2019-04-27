# blog/urls.py
from django.urls import path

from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView

urlpatterns = [
	path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name = 'post_delete'),  # post delte
	path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'),  # post update
	path('post/new/', BlogCreateView.as_view(), name='post_new'),  # new post page
	path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),  # blog post-details page
	path('', BlogListView.as_view(), name='home'),

]