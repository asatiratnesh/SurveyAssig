from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView


# Create your views here.
class AboutView(TemplateView):
    template_name = 'about.html'
