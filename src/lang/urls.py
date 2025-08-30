from django.urls import path 
from . import views
from django.conf.urls.i18n import set_language

app_name = 'lang'

urlpatterns = [
  path('', views.lang , name='lang'),
  path("i18n/setlang/", set_language, name="set_language"),

]
