from typing import Optional
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,

    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.utils import timezone

from .models import News
from animals.models import Animal
from users.models import Profile
from shelters.models import Shelter

def home(request):
    """Returns the three most recent posts and animals to render home page"""
    latest_news = News.objects.order_by("-date_created")[:3]
    latest_animals = Animal.objects.order_by("-date_entered")[:3]

    context = {
        'news': latest_news,
        'animals': latest_animals,
    }

    return render(request, 'news/home.html', context=context)

# Create your views here.
class NewsDetailView(DetailView):
    model = News

class NewsListView(ListView):
    model = News
    ordering = ['-date_created']
    paginate_by = 5

class NewsCreateView(LoginRequiredMixin, CreateView):
    model = News
    fields = [
        "title",
        "body",
        "animal"
    ]
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        profile = self.request.user.profile
        if profile.shelter:
            form.fields['animal'].queryset = Animal.objects.filter(shelter=profile.shelter)
        return form
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class NewsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = News
    fields = [
        "title",
        "body",
        "animal"
    ]

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        profile = self.request.user.profile
        if profile.shelter:
            form.fields['animal'].queryset = Animal.objects.filter(shelter=profile.shelter)
        return form

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        news = self.get_object()
        if self.request.user == news.author:
            return True
        return False

class NewsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = News
    success_url = '/news/'

    def test_func(self):
        news = self.get_object()
        if self.request.user == news.author:
            return True
        return False