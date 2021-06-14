from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView
from .models import Post
from .models import Slide


class HomePageView(ListView):
    model=Slide
    context_object_name = 'Slides'
    template_name = 'home.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

def chat(request):
    return render(request, 'chat.html')

def room(request, room_name):
    return render(request, 'room.html', {
        'room_name': room_name
    })