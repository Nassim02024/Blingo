from django.urls import path 
from . import views

urlpatterns = [
  path('commingsoon/' , views.commingsoon , name='commingsoon'),
]