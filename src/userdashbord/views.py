from django.shortcuts import render , redirect , HttpResponse
from core.models import Category , Product , CartOrder , User , Vendor
from django.db.models import Sum
from users.models import User
import datetime
from django.contrib.auth.decorators import login_required
from userdashbord.forms import AddProductForms


# @login_required
def dashbord(request):
    vendor = Vendor.objects.get(user=request.user)
    orders = CartOrder.objects.filter(vendor=vendor).order_by('-order_date')
    count_product = Product.objects.filter(vendor=vendor).count
    context = {
        'orders': orders,
        "count_product" : count_product,
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

# def billing(request):
#   return render(request, 'userdashbord/billing.html')

# def profile(request):
#   return render(request, 'userdashbord/profile.html')

def sideBar(request):
  return render(request, 'userdashbord/side-bar.html')

# def sign_in(request):
#   return render(request, 'userdashbord/sign-in.html')

# def sign_up(request):
#   return render(request, 'userdashbord/sign-up.html')




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
    items = order.items.all() 
    print(order.delivry)
    context = {
      'order': order,
      'items': items,
      'lng' : order.lng,
      'lat': order.lat,
      'delivry': order.delivry,
    }
    return render(request, 'userdashbord/orderonecustemor.html' , context)



from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import AddProductForms
import cloudinary.uploader

def addproduct(request):
    if request.method == 'POST':
        form = AddProductForms(request.POST , request.FILES)
        if form.is_valid():
            try:
                new_form = form.save(commit=False)
                new_form.user = request.user
                new_form.vendor = request.user.vendor 
                
                # رفع الصورة على Cloudinary (اختياري حسب حقل الصورة)
                if 'image' in request.FILES:
                    upload_result = cloudinary.uploader.upload(
                        request.FILES['image'],
                        timeout=30  # زيادة وقت الاتصال إذا بطيء
                    )
                    new_form.image = upload_result['secure_url']

                
                new_form.save()
                form.save_m2m()  # لحفظ علاقات ManyToMany
                
                messages.success(request, "تم إضافة المنتج بنجاح!")
                return redirect('dashbord')

            except Exception as e:
                # إذا حدث أي خطأ أثناء الحفظ أو الرفع
                messages.error(request, f"حدث خطأ أثناء إضافة المنتج: {str(e)}")
        else:
            messages.error(request, "البيانات غير صحيحة، يرجى التحقق من النموذج.")
    else:
        form = AddProductForms()

    context = {
        "form": form
    }
    return render(request, 'userdashbord/addproduct.html', context)


# def virtual_reality(request):
#   return render(request, 'userdashbord/virtual-reality.html')
