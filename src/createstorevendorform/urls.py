from django.urls import path 
from . import views

urlpatterns = [
  path('createstorevendorform/', views.createstorevendorform , name='createstorevendorform'),

]
