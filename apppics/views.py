from django.shortcuts import render
from django.http  import Http404,HttpResponseRedirect, request
#from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,HttpResponse
from .forms import FormImage
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate

# Create your views he
from .models import *
#from rest_framework.response import Response
#from rest_framework.views import APIView
#from .serializers import ProjectSerializer,ProfileSerialiser
#from rest_framework.views import APIView
# need

# Create your views here.
def home(request):
    images = Image.get_images()
    
    return render(request, 'home.html' ,{"images":images})



def search():
    if 'image' in request.GET and request.GET['image']:
        search_category = request.GET['image']
        searched = Image.search_by_tag(search_category)
        message = f'{search_category}'

    return render(request, search.html, {"searched":searched, "message":message})
    
    
def locale():
    pass





