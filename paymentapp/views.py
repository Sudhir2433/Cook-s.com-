from django.shortcuts import render,redirect,HttpResponse
from Servicesapp.models import Services
from .models import Aboutyou,ContactDetail,Address,CommonKey
# from .forms import Booknowform
from django.shortcuts import render, get_object_or_404
# Create your views here.
from django.contrib.auth.decorators import login_required
import razorpay

# @login_required(login_url='login')
def quickview(request,labour_id):
    service = get_object_or_404(Services, labour_id=labour_id)
    
    # ... your payment related logic ...
    data={'services': service}
    return render(request, 'quickview.html', data)

# when you will click on quick view
@login_required(login_url='login')
def aboutyou(request):
    if request.method=='POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')  
        common_key = CommonKey.objects.create()

        # Use the common_key when creating the Aboutyou object
        about_you = Aboutyou.objects.create(fname=fname, lname=lname, common_key=common_key)

        # field=Aboutyou(fname=fname,lname=lname)
        about_you.save()
        return redirect('contactDetail')
    return render(request, 'about.html')  

def contactDetail(request):
    if request.method=='POST':
        email = request.POST.get('email')
        number = request.POST.get('number')
        common_key = CommonKey.objects.create()
        about_you = ContactDetail.objects.create(email=email,contact=number, common_key=common_key)
        about_you.save()
        # return redirect('address')

        labour_id = 1  # Replace with the actual labour_id
        return redirect('address', labour_id=labour_id)

    return render(request, 'contactDetail.html')

def address(request,labour_id):
        service = get_object_or_404(Services, labour_id=labour_id)
        # amount=service.Price*100
        # Name=service.Name 
        # data={'services': service,'amount':amount,'Name':Name}
         
    # ... your payment related logic ...
        if request.method=='POST': 
        # key_id,key_secret
            client = razorpay.Client(auth=("rzp_test_Y9yds6XduNMIS1", "FxeCiHxxdalPrHGOsNOCinF6"))

            DATA = {
                "amount":service.Price ,
                "currency": "INR",
                "receipt": "Feelfreetocode123",
                "notes": {
                    "name": service.Name,
                    "payment_for": "Angular course"
                }
            }
            order=client.order.create(data=DATA) 

            address1 = request.POST.get('address1')
            address2 = request.POST.get('address2')
            city = request.POST.get('city')
            state = request.POST.get('state')
            zip = request.POST.get('zip')
            common_key = CommonKey.objects.create()

            # Use the common_key when creating the Address object
            address = Address.objects.create(address1=address1,address2=address2,city=city,state=state,zip=zip,common_key=common_key)
            address.save()
            # return redirect('address')
            
            # data = {'order_id': order['id']}
            # return render(request, 'paynow.html', data)
            return redirect('address', labour_id=labour_id)
        return render(request, 'Address.html', {'service': service})
    

def paynow(request):
    return render(request, 'paynow.html')