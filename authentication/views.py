from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages


def Home(request):
    return render(request, 'home/home.html')    

def Register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
        else:
            user = User.objects.create_user(username=username, password=password)
            messages.success(request, "User registered. Please login.")
            return redirect('login')  
    return render(request, 'auth/register.html')

@csrf_protect
def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, {username}!")
            return redirect('questions')  
        else:
            messages.error(request, "Invalid username or password.")
            
    return render(request, 'auth/login.html')


# Logout
def logout_view(request):
    logout(request)
    return redirect('home')
