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
    
    # ✅ الترتيب صحيح: order_by('-order_date') من الأحدث إلى الأقدم
    orders = CartOrder.objects.filter(vendor_new=vendor).order_by('-order_date')
    
    # ✅ استخدام .count() كدالة
    count_product = Product.objects.filter(vendor=vendor).count() 
    
    context = {
        'orders': orders, 
        "count_product" : count_product,
    }
    return render(request, 'userdashbord/dashbord.html', context)


# دالة عرض جميع الطلبات للتاجر (لوحة تحكم التاجر)
def tables(request):
    product = Product.objects.all() 
    
    vendor = Vendor.objects.get(user=request.user)
    
    # ✅ الترتيب صحيح: order_by('-order_date') من الأحدث إلى الأقدم
    orders = CartOrder.objects.filter(vendor_new=vendor).order_by('-order_date')
    
    context = {
        'orders': orders,
        'product': product,
    }
    return render(request, 'userdashbord/tables.html', context)


# @login_required
# def dashbord(request):
#   vendor = Vendor.objects.get(user= request.user)
#   order = CartOrder.objects.filter(product__vendor = vendor) 
    
    # revenue = CartOrder.objects.aaggregate(product_price = Sum("price"))  # إيرادات 
    # print(revenue)
    # total_order_count = CartOrder.objects.all()
    # all_product = Product.objects.all()
    # all_category = Category.objects.all()
    # new_customer = User.objects.all()
    # last_order = CartOrder.objects.all()
    
    # this_month = datetime.datetime.now().month
    
    # monthly_revenue = CartOrder.objects.filter(order_date__month=this_month).aggregate(Sum("price"))


    # context={
    #   "order" : order,
    #   "revenue" :revenue,
    #   "total_order_count" : total_order_count,
    #   "all_product" : all_product,
    #   "all_category" : all_category,
    #   "new_customer" : new_customer,
    #   "last_order" : last_order,
    #   "monthly_revenue" : monthly_revenue,
    # }
    # print(context)
    # return render(request, 'userdashbord/dashbord.html' , context)

# def billing(request):
#   return render(request, 'userdashbord/billing.html')

# def profile(request):
#   return render(request, 'userdashbord/profile.html')

def sideBar(request):
    return render(request, 'userdashbord/side-bar.html')

# def sign_in(request):
#   return render(request, 'userdashbord/sign-in.html')

# def sign_up(request):
#   return render(request, 'userdashbord/sign-up.html')




from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# تم التأكد من هذا السطر
from decouple import config
import resend # نحافظ على الاستيراد هنا
from django.db.models import Sum
from decimal import Decimal # 👈 تأكد من استيراد هذه المكتبة
# ... (بقية الاستيرادات مثل CartOrder, Vendor, Product)

def tables(request):
    vendor = Vendor.objects.get(user=request.user)
    
    orders_qs = CartOrder.objects.filter(vendor_new=vendor).order_by('-order_date')
    
    orders_with_total = []
    
    for order in orders_qs:
        aggregation = order.items.aggregate(
            items_total=Sum('total'),
            items_quantity=Sum('quantity')
        )
        
        # استخراج الإجمالي الكلي لأسعار المنتجات 
        # نستخدم Decimal('0.00') كقيمة افتراضية لضمان أن total_items_price هو دائماً Decimal
        total_items_price = aggregation['items_total'] or Decimal('0.00')
        
        # إضافة الحقول المحسوبة إلى كائن الطلب ديناميكياً
        order.items_total = total_items_price
        
        # 🌟🌟 إدارة حقل التوصيل (delivry) 🌟🌟
        if order.delivry is not None:
            # نحول قيمة delivry (float) إلى Decimal لجمعها مع total_items_price
            # نستخدم str() لتجنب أخطاء الدقة العائمة (floating-point precision errors)
            delivery_price = Decimal(str(order.delivry))
        else:
            delivery_price = Decimal('0.00')
            
        # الجمع الآن يعمل (Decimal + Decimal)
        order.calculated_total = total_items_price + delivery_price
        
        orders_with_total.append(order)
        
    product = Product.objects.all() 
    
    context = {
        'orders': orders_with_total, 
        'product': product,
    }
    return render(request, 'userdashbord/tables.html', context)
# دالة عرض تفاصيل طلب واحد محدد للتاجر
def orderonecustemor(request , id):
    vendor = Vendor.objects.get(user=request.user)
    
    # ✅ الفلترة: التأكد من أن الطلب ينتمي لهذا التاجر
    order = get_object_or_404(CartOrder, vendor_new=vendor , id=id) 
    
    # جلب عناصر الطلب
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
# (دالة addproduct لم تطلب تعديلها ولكن تم إبقاؤها كمرجع)
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import AddProductForms
import cloudinary.uploader
 
def addproduct(request):
    # جلب التاجر المرتبط بالمستخدم الحالي أولاً
    try:
        current_vendor = request.user.vendor
    except Exception:
        messages.error(request, "لا يوجد متجر مرتبط بهذا الحساب.")
        return redirect('dashbord')

    if request.method == 'POST':
        # نمرر التاجر للـ Form هنا أيضاً ليتأكد من صحة التصنيف المختار
        form = AddProductForms(request.POST, request.FILES, vendor=current_vendor)
        if form.is_valid():
            try:
                new_form = form.save(commit=False)
                new_form.user = request.user
                new_form.vendor = current_vendor 
                
                if 'image' in request.FILES:
                    upload_result = cloudinary.uploader.upload(
                        request.FILES['image'],
                        timeout=30
                    )
                    new_form.image = upload_result['secure_url']
                
                new_form.save()
                form.save_m2m()
                
                messages.success(request, "تم إضافة المنتج بنجاح!")
                return redirect('dashbord')

            except Exception as e:
                messages.error(request, f"حدث خطأ أثناء إضافة المنتج: {str(e)}")
        else:
            messages.error(request, "البيانات غير صحيحة، يرجى التحقق من النموذج.")
    else:
        # هنا التمرير الأهم لإظهار التصنيفات الصحيحة في صفحة الإضافة (GET)
        form = AddProductForms(vendor=current_vendor)

    context = {
        "form": form
    }
    return render(request, 'userdashbord/addproduct.html', context)


# def virtual_reality(request):
#   return render(request, 'userdashbord/virtual-reality.html')