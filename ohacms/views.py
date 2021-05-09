from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from .models import Post


class HomePageView(TemplateView):
    template_name = 'home.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
