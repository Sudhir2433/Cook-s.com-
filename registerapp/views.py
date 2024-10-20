

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import send_mail
from .models import Register

def send_registration_email(username, email):
    subject = 'Welcome to Our Website'
    message = f'Hi {username},\n\nThank you for registering on our website.'
    from_email = 'guptas8846@gmail.com'
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        if pass1 != pass2:
            messages.error(request, "Passwords do not match")
            return render(request, 'register.html')
        
        if User.objects.filter(username=username).exists():
            messages.warning(request, "Username already exists")
            return render(request, 'register.html')
        
        user = User.objects.create_user(username=username, email=email, password=pass1, first_name=fname, last_name=lname)
        user.save()
        

        
        messages.success(request, "Account created successfully.")
        return redirect('login')
    else:
        return render(request, 'register.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass1')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('services')  # Replace 'services' with your actual home page after login
        else:
            messages.error(request, "Invalid username or password")
            return render(request, 'login.html')
    return render(request, 'login.html')

@login_required
def user_logout(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('home')

