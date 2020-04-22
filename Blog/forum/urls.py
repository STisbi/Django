from django.urls import path
from . import views

urlpatterns = [
    path('',                      views.IndexView.as_view(),            name='index'),
    path('blogs/',                views.BlogListView.as_view(),         name='blogs'),
    path('blog/<int:pk>',         views.BlogDetailView.as_view(),       name='blog-detail'),
    path('blog/<int:pk>/comment', views.AddCommentView.as_view(),       name='add-comment'),
    path('authors/',              views.AuthorListView.as_view(),       name='authors'),
    path('author/<int:pk>',       views.BlogListByAuthorView.as_view(), name='blog-list-by-author'),
    path('add_blog',              views.AddBlogView.as_view(),          name='add-blog'),
    path('add_author',            views.AddAuthorView.as_view(),        name='add-author'),
]