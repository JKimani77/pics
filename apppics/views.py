from django.shortcuts import render
from django.http  import Http404,HttpResponseRedirect
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
    pass
def locale():
    pass

def post(request):
    '''
    view function to post images
    '''
    if request.method=='POST':
        form = FormImage(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            return redirect(home)
    else:
        form = FormImage()
    return render(request, 'newpic.html',{"form":form})



