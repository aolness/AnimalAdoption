from typing import Any
from django.db import models
from django.db.models import F
from django.shortcuts import render, get_object_or_404, render
from django.views import generic
from django.urls import reverse
from django.http import request
from django.shortcuts import render
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.contrib.sites.shortcuts import get_current_site
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User

from .models import Animal, Shelter


class AnimalCreateView(LoginRequiredMixin, CreateView):
    model = Animal
    fields = [
        "name",
        "species",
        "age",
        "breed",
        "availability",
        "disposition",
        "size",
        "image"
    ]

    def get_context_data(self, *args, **kwargs):
        context = super(AnimalCreateView, self).get_context_data(*args, **kwargs)
        context['title'] = "Add a new animal to your shelter"
        return context

    def form_valid(self, form):
        form.instance.shelter = self.request.user.profile.shelter
        form.save()
        response = super().form_valid(form)
        animal = self.object 
        if str(animal.availability) == "Available":
            self.send_email(animal)
        return response
    
    def send_email(self, animal):
            current_site = get_current_site(self.request)
            domain = current_site.domain
            animal_detail_url = f"http://{domain}{animal.get_absolute_url()}"
            subject = 'New Animal Available!'
            html_message = render_to_string('animal_email.html', {'animal': animal, 'animal_detail_url': animal_detail_url})
            from_email = 'PawfectMatch@gmail.com'
            # recipient_list = ['can place your email here for testing']
            recipient_list = User.objects.values_list('email', flat=True)
            for recipient in recipient_list:
                send_mail(subject, html_message, from_email, [recipient], html_message=html_message)


class AnimalUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Animal
    fields = [
        "name",
        "species",
        "age",
        "breed",
        "availability",
        "disposition",
        "size",
        "image"
    ]

    def test_func(self):
        """Check that the user is associated with the same shelter as the animal"""
        animal = self.get_object()
        if self.request.user.profile.shelter == animal.shelter:
            return True
        else:
            return False


class AnimalDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Deletes the posts and redirects to home."""
    model = Animal
    success_url = '/animals'

    def test_func(self):
        """Check that the user is associated with the same shelter as the animal"""
        animal = self.get_object()
        if self.request.user.profile.shelter == animal.shelter:
            return True
        else:
            return False
    

class AnimalListView(generic.ListView):
    model = Animal
    context_object_name = 'animals'


class AnimalDetailView(generic.DetailView):
    model = Animal
    context_object_name = 'animal'

    def get(self, request, *args, **kwargs):
        animal = self.get_object()
        Animal.objects.filter(pk=animal.pk).update(views=F('views') + 1)
        return super().get(request, *args, **kwargs)

