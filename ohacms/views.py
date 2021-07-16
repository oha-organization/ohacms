from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView
from .models import Post
from .models import Slide
from rest_framework import generics, viewsets
from rest_framework import permissions
from ohacms.serializers import PostSerializer, OptionSerializer

class HomePageView(ListView):
    model=Slide
    context_object_name = 'Slides'
    template_name = 'home.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class PostViewSet(generics.ListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    #permission_classes = [permissions.IsAuthenticated]

class PostDetailViewSet(generics.RetrieveAPIView):
    queryset=Post.objects.all()
    serializer_class = PostSerializer
