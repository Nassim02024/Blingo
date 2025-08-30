from django.shortcuts import render , redirect , HttpResponse
from core.models import Category , Product , CartOrder , User , Vendor
from django.db.models import Sum
from users.models import User
import datetime
from django.contrib.auth.decorators import login_required



@login_required
def dashbord(request):
    vendor = Vendor.objects.get(user=request.user)

    orders = CartOrder.objects.filter(vendor=vendor).order_by('-order_date')
    context = {
        'orders': orders,
    }
    return render(request, 'userdashbord/dashbord.html', context)



# @login_required
# def dashbord(request):
#   vendor = Vendor.objects.get(user= request.user)
#   order = CartOrder.objects.filter(product__vendor = vendor) 
  
  # revenue = CartOrder.objects.aaggregate(product_price = Sum("price"))  # إيرادات 
  # print(revenue)
  # total_order_count = CartOrder.objects.all()
  # all_product = Product.objects.all()
  # all_category = Category.objects.all()
  # new_customer = User.objects.all()
  # last_order = CartOrder.objects.all()
  
  # this_month = datetime.datetime.now().month
  
  # monthly_revenue = CartOrder.objects.filter(order_date__month=this_month).aggregate(Sum("price"))


  # context={
  #   "order" : order,
  #   "revenue" :revenue,
  #   "total_order_count" : total_order_count,
  #   "all_product" : all_product,
  #   "all_category" : all_category,
  #   "new_customer" : new_customer,
  #   "last_order" : last_order,
  #   "monthly_revenue" : monthly_revenue,
  # }
  # print(context)
  # return render(request, 'userdashbord/dashbord.html' , context)

def billing(request):
  return render(request, 'userdashbord/billing.html')

def profile(request):
  return render(request, 'userdashbord/profile.html')

def rtl(request):
  return render(request, 'userdashbord/rtl.html')

def sign_in(request):
  return render(request, 'userdashbord/sign-in.html')

def sign_up(request):
  return render(request, 'userdashbord/sign-up.html')




def tables(request):
    product = Product.objects.all()
    vendor = Vendor.objects.get(user=request.user)
    orders = CartOrder.objects.filter(vendor=vendor).order_by('-order_date')
    context = {
        'orders': orders,
        'product': product,
    }
    return render(request, 'userdashbord/tables.html', context)




def orderonecustemor(request , id):
    vendor = Vendor.objects.get(user=request.user)
    order = CartOrder.objects.get(vendor=vendor , id=id)
    items = order.items.all()  # related_name='items'
    context = {
        'order': order,
        'items': items,
    }
    return render(request, 'userdashbord/orderonecustemor.html' , context)


def virtual_reality(request):
  return render(request, 'userdashbord/virtual-reality.html')
