from django.conf.urls import url

from . import views
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

urlpatterns = [
    url(r'^$', views.index, name='index'),
]