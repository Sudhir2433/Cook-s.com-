from django.shortcuts import render,HttpResponse

# Create your views here.

# your_app_name/views.py
from django.shortcuts import render, redirect
from .forms import RegistrationForm,LoginForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User

# views.py or any other Python file where you want to send the email
from django.core.mail import send_mail

def send_registration_email(username, email):
    subject = 'Welcome to Our Website'  # Subject of the email
    message = f'Hi {username},\n\nThank you for registering on our website.'  # Email message
    from_email = 'guptas8846@gmail.com'  # Replace with your email address
    recipient_list = [email]  # Email recipient(s)
    send_mail(subject, message, from_email, recipient_list)






def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            user=User.objects.filter(username=username)
            if user.exists():
                messages.warning(request, "Username is already exist.")
                return redirect('')
            user1=form.save()            
            messages.warning(request, "Acount create successfuly")
            # send_registration_email(user1.username, user1.email)
            return redirect('login')  # Redirect to a success page after registration.

    else:
        form = RegistrationForm()
        return render(request, 'register.html', {'form': form})
    
    return render(request, 'register.html')
    
def user_login(request):
    

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        messages.success(request,"Login successfully")
        user = authenticate(username=username, password=password) #ye hme ye chek kerke dega ki jo hum password dal rhe hai vo shi hai ya nhi

        if user is not None:
            login(request, user)

            return redirect('services')  # Replace 'home' with the URL name of the home page after login.
        else:
            # Handle invalid login credentials, e.g., display an error message.
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')

@login_required()
def user_logout(request):
    logout(request)
    messages.success(request,"Logout successfully")
    return redirect('home')
