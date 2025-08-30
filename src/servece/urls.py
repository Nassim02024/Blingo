from django.urls import path 
from . import views
urlpatterns = [
  path("servece/", views.servece, name="servece")
]
