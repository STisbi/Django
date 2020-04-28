from datetime import date

from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from .models import Blog, BlogUser, Comment


# Create your views here.
class IndexView(generic.TemplateView):
    template_name = 'index.html'

    number_of_blogs = Blog.objects.all().count()
    number_of_authors = BlogUser.objects.all().count()
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
    model = BlogUser


class BlogListByAuthorView(generic.ListView):
    model = Blog
    template_name = 'forum/blog_list_by_author.html'


    def get_queryset(self):
        """
        Return list of Blog objects created by BlogAuthor (author id specified in URL)
        """
        id = self.kwargs['pk']
        target_author = get_object_or_404(BlogUser, pk=id)

        return Blog.objects.filter(author=target_author)

    def get_context_data(self, **kwargs):
        """
        Add BlogAuthor to context so they can be displayed in the template
        """
        # Call the base implementation first to get a context
        context = super(BlogListByAuthorView, self).get_context_data(**kwargs)

        # Get the blogger object from the "pk" URL parameter and add it to the context
        context['blogger'] = get_object_or_404(BlogUser, pk=self.kwargs['pk'])

        return context


class AddCommentView(LoginRequiredMixin, generic.CreateView):
    model = Comment
    fields = ['comment']

    def form_valid(self, form):
        blog_id = self.kwargs['pk']

        form.instance.post_date = date.today()
        form.instance.blog = get_object_or_404(Blog, pk=blog_id)
        form.instance.author = self.request.user

        return super(AddCommentView, self).form_valid(form)

    def get_success_url(self):
        return reverse(viewname='blog-detail', kwargs={'pk': self.kwargs['pk']})


class AddBlogView(LoginRequiredMixin, generic.CreateView):
    model = Blog
    fields = ['title', 'entry']

    def form_valid(self, form):
        form.instance.post_date = date.today()
        form.instance.author = BlogUser.objects.get(user=self.request.user)

        return super(AddBlogView, self).form_valid(form)

    def get_success_url(self):
        return reverse(viewname='blogs')


class AddAuthorView(generic.CreateView):
    model = BlogUser
    fields = ['username', 'password', 'biography']

    def get_success_url(self):
        return reverse(viewname='index')
