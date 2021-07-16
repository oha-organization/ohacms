from django.urls import path
from ohacms.api import views


urlpatterns = [
    
    path('api/posts', views.PostViewSet),

]

