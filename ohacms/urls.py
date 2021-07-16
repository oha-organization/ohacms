from django.urls import path
from .views import HomePageView, PostDetailView, PostViewSet, PostDetailViewSet



urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('post/<slug:slug>', PostDetailView.as_view(),name='post-detail'),
    path('api/posts', PostViewSet.as_view(),name='arif'),
    path('api/posts/<int:pk>', PostDetailViewSet.as_view(),name='ceylan'),
]

