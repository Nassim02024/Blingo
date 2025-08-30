from django.urls import path 
from . import views

urlpatterns = [
   path('customer/' , views.customer , name="customer"),
   path('detilsview/<int:id>' , views.detilsview , name="detilsview")
]