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
            user = form.save()  # حفظ المستخدم
            login(request, user)  # تسجيل الدخول مباشرة
            messages.success(request, f"Your account was created successfully, {user.username}!")
            return redirect("index")  # تحويل للصفحة الرئيسية
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
            return render(request, "users/login.html")
        
        userauth = authenticate(request, username=user.username, password=password)
        if userauth is not None:
            login(request, userauth)
            messages.success(request, 'You are logged in.')
            return redirect("core:index")
        else:
            messages.warning(request, 'Email or password is incorrect.')

    return render(request, "users/login.html")


def logout_view(request):
    logout(request)
    return redirect("users:register")



# User = get_user_model()

# def register(request):
#   if request.method == 'POST':
#     try:
#       form = SingUpForm(request.POST)
#       if form.is_valid():
#         email = form.cleaned_data.get('email')
#         username = form.cleaned_data.get('username')
#         password = form.cleaned_data.get('password1')
#         if not User.objects.filter(email=email).exists():      
#           saved_user = form.save()
#           new_user = authenticate(username=username  , password=password)
#           login(request  , new_user)
#           messages.success(request , f"your account created successfully {username}")
#           print("your account created successfully")
#           return redirect("core:index" )
#         else:
#           print("البريد موجود بالفعل") 
#           return render(request , "users/register.html")
#     except:
#       return render(request , "users/register.html")       
#   else: 
#     form = SingUpForm()
#     print("cant rejester")

  
#   context={
#     'form':form
#   }
#   return render(request , "users/register.html" , context)


# def login_view(request):
  
#   if request.method == 'POST':
#     form = SingUpForm(request.POST)
#     email = request.POST.get('email') 
#     password = request.POST.get('password')
#     try:
#       user = User.objects.get(email=email)
#     except:
#       messages.warning(request, 'Email is incorrect.') 
    
#     if user:
#       userauth = authenticate(request , email=email , password=password)  
#       if userauth is not None:
#         login(request , userauth)
#         messages.success(request , 'You are logged in.')
#         return redirect("index")
#     else:
#       messages.warning(request, 'Email or password is incorrect.')
#       return HttpResponse("Email or password is incorrect.")
#   context={
#     'form':form
#   }
#   return render(request , "users/register.html" , context )      


# def logout_view(request):
#   logout(request)
#   return redirect("users:register")


