from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView
from .models import Post
from .models import Slide
from django.http import HttpResponse

class HomePageView(ListView):
    model=Slide
    context_object_name = 'Slides'
    template_name = 'home.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class AjaxTest(TemplateView):
    template_name = 'ajaxtest.html'

def ajax_request(request):
    return HttpResponse('result')

