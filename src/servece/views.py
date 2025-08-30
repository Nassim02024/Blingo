from django.shortcuts import render
from django.views.decorators.cache import cache_page

@cache_page(60 * 60 * 24 * 365)
def servece(request):
    return render(request, 'servece/servece.html')
