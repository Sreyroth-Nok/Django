from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .form import SignUpForm  # Make sure your form is named correctly (SignUpForm)

def home(request):
    # Check if the user is submitting the login form
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have been logged in')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('home')

    return render(request, 'home.html')

def login_user(request):
    # Optional custom login view (not currently used)
    return redirect('home')

def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')  # default name in UserCreationForm
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, 'You have been registered and logged in')
            return redirect('home')
    else:
        form = SignUpForm()

    return render(request, 'register.html', {'form': form})
