from django.shortcuts import render
from django.http  import Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,HttpResponse
#from .forms import LoginForm,ProjectForm,ProfileForm,RatingForm
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
def index(request):
    images = Image.get_images()
    location = Location.objects.all()
    return render(request, 'home.html' ,{"images":images})

# Create your views here.


