from django.urls import path 
from . import views


urlpatterns = [
  path('', views.index , name='index'),
  path('products/', views.products , name='products'),
  path('product/<uuid:vid>/', views.product , name='product'),
  path('category/<uuid:vid>/', views.category , name='category'),
  path('product_category/<uuid:cid>/', views.product_category , name='product_category'),
  path('vendor/', views.vendor , name='vendor'),
  path('productDetils/<uuid:pid>', views.productDetils , name='productDetils'),
  path('search_vendor/', views.search_vendor , name='search_vendor'),
  path('search_product/<uuid:vid>', views.search_product, name='search_product'),
  path('cardorder/<uuid:vid>/', views.cardorder , name='cardorder'),


  # path('vendor_orders/', views.vendor_orders , name='vendor_orders'),

]
