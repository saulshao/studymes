from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from .models import *

def index(request):
    #return HttpResponse("Hello, world. You're at the factory index.")
    return  render_to_response('region.html', {"subregions":Region.objects.filter(parent = None)})
