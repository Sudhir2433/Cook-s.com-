
# Create your views here.
from django.shortcuts import render,redirect,HttpResponseRedirect,get_object_or_404
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import CookRegistrationForm,SearchForm
from Servicesapp.models import Services
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# for paginator
from django.core.paginator import Paginator

'''{ for update import comment

 from django.shortcuts import render, get_object_or_404, redirect
 from .models import YourModel
 from .forms import YourModelForm }'''


# @login_required(login_url='login')
def services(request):
    ServiceData=Services.objects.all()
    print(ServiceData)
    if request.method=="GET":
        Search=request.GET.get('search')
        if Search!=None:
            
            ServiceData=Services.objects.filter(Name__icontains=Search)
            # print(request.GET.get('search'))
            # print(ServiceData)
        
    paginator=Paginator(ServiceData,6)
    page_number=request.GET.get('page')
    ServiceDataFinal=paginator.get_page(page_number)
    totalpage=ServiceDataFinal.paginator.num_pages
    
    data={
        'ServiceData':ServiceDataFinal,
        'TotalPageList':[n+1 for n in range(totalpage)],
      
    }
    return render(request,"services.html",data)
   


from django.shortcuts import render, redirect
from .forms import CookRegistrationForm

def CookRegistation(request):
    if request.method == 'POST':
        form = CookRegistrationForm(request.POST, request.FILES)  # Include request.FILES here
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to the home page after successful registration
    else:
        form = CookRegistrationForm()

    return render(request, 'CookRegistation.html', {'form': form})


# Views for search

