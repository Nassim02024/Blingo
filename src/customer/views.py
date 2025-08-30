from django.shortcuts import get_object_or_404, render
from core.models import Vendor , CartOrder  , CartOrderItems
from users.models import User

def dashbord(request):
  return render(request , 'customer/dashbord.html')




def customer(request):
    user = get_object_or_404(User, username=request.user.username)
    order = CartOrder.objects.filter(user=request.user)
    vendor = Vendor.objects.all()
    context = {
      'vendor': vendor,
      'order': order,
      'user': user,
      
    }
    return render(request, 'customer/customer.html', context)




def detilsview(request , id):
    order = CartOrder.objects.filter(id=id, user=request.user).first()
    products = CartOrderItems.objects.filter(order=order)

    context = {
      'products': products,
    }
    return render(request, 'customer/detilsview.html' , context)
