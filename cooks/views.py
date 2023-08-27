

# Create your views here.
from django.shortcuts import render,redirect,HttpResponse
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import ContactForm
from cooks.models import News
from cooks.models import contactEnquiry
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
def home(request):
    return render(request,"home.html")
def about(request):
    newsdata=News.objects.all()
    data={
        'NewsData':newsdata
    }
    return render(request,"aboutus.html",data)
# @login_required(login_url='login')
# def services(request):
#     return render(request,"services.html")


def contact(request):
    if request.method=='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Registered successfully')
            return redirect('contact')
    else:
      form =ContactForm()    
    return render(request,"contact.html",{'form':form})





