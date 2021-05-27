from django.urls import path
from .views import HomePageView, PostDetailView,AjaxTest, ajax_request



urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('post/<slug:slug>', PostDetailView.as_view(),name='post-detail'),
    path('ajaxtest',AjaxTest.as_view()),
    path('ajax_request',ajax_request),
]

