from django.urls import path 
from . import views

urlpatterns = [
  path('dashbord/', views.dashbord , name='dashbord'),
  path('billing/', views.billing , name='billing'),
  path('profile/', views.profile , name='profile'),
  path('rtl/', views.rtl , name='rtl'),
  path('sign_in/', views.sign_in , name='sign_in'),
  path('sign_up/', views.sign_up , name='sign_up'),
  path('tables/', views.tables , name='tables'),
  path('virtual_reality/', views.virtual_reality , name='virtual_reality'),
  path('orderonecustemor/<int:id>/', views.orderonecustemor , name='orderonecustemor'),
  # path('vendor_orders/', views.vendor_orders , name='vendor_orders'),

]