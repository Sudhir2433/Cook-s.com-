from django.shortcuts import render,redirect
from Servicesapp.models import Services
# from .models import BookNow
# from .forms import Booknowform
from django.shortcuts import render, get_object_or_404
# Create your views here.



def quickview(request,labour_id):
    service = get_object_or_404(Services, labour_id=labour_id)

    # ... your payment related logic ...

    return render(request, 'quickview.html', {'service': service})