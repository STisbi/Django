from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Blog, Author, Comment

# Create your views here.
class IndexView(generic.TemplateView):
    template_name = 'index.html'

    number_of_blogs = Blog.objects.all().count()
    number_of_authors = Author.objects.all().count()
    number_of_comments = Comment.objects.all().count()

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(IndexView, self).get_context_data(**kwargs)

        # Create any data and add it to the context
        context['number_of_blogs'] = self.number_of_blogs
        context['number_of_authors'] = self.number_of_authors
        context['number_of_comments'] = self.number_of_comments

        return context


class BlogListView(generic.ListView):
    model = Blog


class BlogDetailView(generic.DetailView):
    model = Blog


class AuthorListView(generic.ListView):
    model = Author


class BlogListByAuthorView(generic.ListView):
    model = Blog
    template_name = 'forum/blog_list_by_author.html'


    def get_queryset(self):
        """
        Return list of Blog objects created by BlogAuthor (author id specified in URL)
        """
        id = self.kwargs['pk']
        target_author = get_object_or_404(Author, pk=id)

        return Blog.objects.filter(author=target_author)

    def get_context_data(self, **kwargs):
        """
        Add BlogAuthor to context so they can be displayed in the template
        """
        # Call the base implementation first to get a context
        context = super(BlogListByAuthorView, self).get_context_data(**kwargs)

        # Get the blogger object from the "pk" URL parameter and add it to the context
        context['blogger'] = get_object_or_404(Author, pk=self.kwargs['pk'])

        return context