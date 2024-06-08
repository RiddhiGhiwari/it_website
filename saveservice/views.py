from django.shortcuts import render,redirect
from .models import mymodel
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect
import json

# Create your views here.

def index(request):
    return render(request,'index.html',{})

def about(request):
    return render(request,'about.html',{})

def services(request):
    return render(request,'services.html',{})

@csrf_exempt
def savecontact(request):

    #print("requuest"+ str(request.body))
    if request.method=='POST':
        data = json.loads(request.body)
        name=data['name']
        phone=data['phone']
        email=data['email']
        message=data['message']

        

       
        
        
     
        
        
        user = mymodel(name=name,email=email, phone=phone, message=message)
        print(user)
        user.save()
        print('user created')
        return render(request,'contact.html',{})
        
    else:
        return render(request,'contact.html',{})


def contact(request):

    return render(request,'contact.html',{})

def blog(request):
    return render(request,'blog.html',{})

def careers(request):
    return render(request,'careers.html',{})













