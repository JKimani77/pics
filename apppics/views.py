from django.shortcuts import render

from django.shortcuts import render,HttpResponse

from django.template import loader


from .models import *



def home(request):
    images = Image.get_images()
    
    return render(request, 'home.html' ,{"images":images})



def search(request):
    '''View function to search by category'''
    template = loader.get_template('search.html')
    if 'image' in request.GET and request.GET['image']:
        _category = request.GET['image']
        searched = Image.search_images(_category)
        message = f'{_category}'

        context = {
            'message': message,
            'images': searched,
        }
        return HttpResponse(template.render(context,request))

    else:
        message = 'The category does not exist!!'

        context = {
            'message': message,
        }
        return render(request, 'search.html', {'message': message})
def locale():
    pass





