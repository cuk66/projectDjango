from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('relevance', views.relevance, name='relevance'),
    path('skills', views.skills, name='skills')
]
