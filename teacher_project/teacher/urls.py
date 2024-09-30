
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
from django.shortcuts import render

def index(request):
    return render(request, 'teacher/index.html')
