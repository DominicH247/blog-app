# blog/urls.py
from django.urls import path

from .views import BlogListView, BlogDetailView

urlpatterns = [
	path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),  # blog post-details page
	path('', BlogListView.as_view(), name='home'),

]