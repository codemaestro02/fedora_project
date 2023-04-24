from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from .views import index, blog_search, blog_create ,search, blog_detail, BlogPostDetailView, BlogPostCreateView, BlogPostListView, BlogPostUpdateView, like_view

urlpatterns = [
    path("", index, name="blog_index"),
    path("blogs/", BlogPostListView.as_view(), name="blog_list"),
    # path('blogs/search/', search, name="blog_list"),
    path('blogs/<slug:slug>/', blog_detail, name='blog_detail'),
    path('create/', blog_create, name='blog_create'),
    path('<str:slug>/update/', BlogPostUpdateView.as_view(), name='blog_update'),
    
    path('blogs/<slug:slug>/like/', like_view, name="blog_like")
    

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
