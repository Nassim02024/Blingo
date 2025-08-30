from django.shortcuts import render

# Create your views here.

def errorpage(request):
    return render(request, 'errorpage/errorpage.html')