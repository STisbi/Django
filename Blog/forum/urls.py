from django.urls import path
from . import views

urlpatterns = [
    path('',                views.IndexView.as_view(),            name='index'),
    path('blogs/',          views.BlogListView.as_view(),         name='blogs'),
    path('blog/<int:pk>',   views.BlogDetailView.as_view(),       name='blog-detail'),
    path('authors/',        views.AuthorListView.as_view(),       name='authors'),
    path('author/<int:pk>', views.BlogListByAuthorView.as_view(), name='blog-list-by-author'),
]