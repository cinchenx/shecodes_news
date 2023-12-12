from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.views import generic
from django.urls import reverse_lazy
from .models import NewsStory
from .forms import StoryForm
from users.models import CustomUser
from .forms import AddComment

# consider views like request handlers

class IndexView(generic.ListView):
    template_name = 'news/index.html'
    context_object_name = "all_stories"

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.all().order_by('-pub_date')[:4]
        context['all_stories'] = NewsStory.objects.all()
        return context

class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'


    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['form']=AddComment()
        return context

class AddStoryView(generic.CreateView):
    form_class = StoryForm
    context_object_name = 'storyform'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# create new class to view all stories by a certain author

class AuthorStories(generic.ListView):
    model = NewsStory
    template_name = 'news/authorStories.html'

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.filter(author_id=self.kwargs['pk'])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.all().filter(author_id=self.kwargs['pk']).order_by('-pub_date')
        context['author'] = CustomUser.objects.get(id=self.kwargs['pk'])
        return context


# need add comment view

class AddCommentView(generic.CreateView):
    form_class = AddComment
    template_name = 'news/story.html'    
    

    def form_valid(self, form):
        form.instance.author = self.request.user
        pk =self.kwargs.get("pk")
        form.instance.story = get_object_or_404 (NewsStory,pk=pk)
        return super().form_valid(form)
    
 
    def get_success_url(self):
        return reverse_lazy("news:story", kwargs={"pk":self.kwargs.get("pk")})




    

    
