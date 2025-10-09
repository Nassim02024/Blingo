from django.http import HttpResponse 
from django.shortcuts import render , redirect 

from django.contrib.auth import get_user_model, login, authenticate, logout
from django.contrib import messages
from .forms import SignUpForm

User = get_user_model()


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()  
            login(request, user)  
            messages.success(request, f"Your account was created successfully, {user.username}!")
            return redirect("index")  
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = SignUpForm()
    
    return render(request, "users/register.html", {'form': form})


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.warning(request, 'Email or password is incorrect.')
            return render(request, "users/register.html")
        
        userauth = authenticate(request, email=email , password=password)
        if userauth is not None:
            login(request, userauth)
            messages.success(request, 'You are logged in.')
            return redirect("index")
        else:
            messages.warning(request, 'Email or password is incorrect.')

    return render(request, "users/register.html")


def logout_view(request):
    logout(request)
    return redirect("users:register")


