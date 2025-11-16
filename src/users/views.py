from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, authenticate, logout
from django.contrib import messages
from .forms import SignUpForm

User = get_user_model()

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()

            # ✅ المصادقة بالبريد الإلكتروني بدلاً من اسم المستخدم
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, f"Your account was created successfully, {user.email}!")
                return redirect("index")
            else:
                messages.error(request, "Account created, but login failed. Please log in manually.")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = SignUpForm()

    return render(request, "users/register.html", {'form': form})


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # ✅ استخدام authenticate مباشرة، لا داعي لجلب user يدويًا
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'You are logged in.')
            return redirect("index")
        else:
            messages.warning(request, 'Email or password is incorrect.')

    return render(request, "users/register.html")


def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect("users:register")
