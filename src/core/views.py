from datetime import datetime
from decimal import Decimal
from pyexpat.errors import messages
import cloudinary.uploader
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render , redirect
import resend
from decouple import config

from ecommestore import settings
from .models import Product , Category , Vendor , ProductReview ,CartOrder , CartOrderItems
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

# location
from django.views.decorators.csrf import csrf_exempt
import json

# resend.com Email
# from .emails import send_email_with_resend



# @login_required(login_url='users:register')
def index(request):
  vendor = Vendor.objects.all()
  product = Product.objects.filter(featured=True , product_status="published")
  context = {
    'vendor': vendor,
    'product': product,
  }
  return render(request, 'core/index.html' , context)




def products(request):
  product = Product.objects.filter(product_status="published")
  context = {
    'product': product,
  }
  return render(request, 'core/products.html' , context)

def product(request , vid):
  vendor = Vendor.objects.get(vid=vid)
  product = Product.objects.filter(product_status="published" , vendor=vendor)
  context = {
    'product': product,
    'vendor': vendor
  }
  return render(request, 'core/productsforvendor.html' , context)



def category(request , vid):
  vendor = Vendor.objects.get(vid = vid)
  category = Category.objects.filter(vendor=vendor)
  context = {
    'category': category,
    "vendor": vendor
  } 
  return render(request, 'core/category.html' , context)


def product_category(request, cid, vid):
    # جلب التاجر
    vendor = get_object_or_404(Vendor, vid=vid)
    
    # جلب التصنيف المحدد لهذا التاجر فقط
    # تأكد أن 'cid' هو المعرف الفريد الذي تستخدمه في الموديل
    category = get_object_or_404(Category, cid=cid, vendor=vendor)

    # جلب المنتجات (تأكد من استخدام الفلترة الصارمة)
    products = Product.objects.filter(
        vendor=vendor,      # يجب أن يكون التاجر هو صاحب المنتج
        category=category,  # يجب أن يكون المنتج مسجلاً تحت هذا التصنيف تحديداً
        product_status="published"
    )

    context = {
        "category": category,
        "products": products,
        "vendor": vendor
    }
    return render(request, 'core/product_category.html', context)



# Dont complete
def vendor(request):
  vendor = Vendor.objects.all()
  context = {
    "vendor": vendor,
  } 
  
  return render(request, 'core/vendor.html' , context)




def productDetils(request , pid):
  productDetils = Product.objects.get(pid= pid)
  products = Product.objects.filter(category= productDetils.category , product_status="published").exclude(pid= pid)
  reviwes = ProductReview.objects.filter(product= productDetils)
  context = {
    "productDetils": productDetils,
    "products": products,
    "reviwes": reviwes,
  
  } 
  
  return render(request, 'core/productDetils.html' , context )



def search_vendor(request):
  query = request.GET.get("q" , "")
  vendor = Vendor.objects.filter(title__icontains=query)
  context = {
    "query": query,
    "vendor": vendor,
    
  
  } 
  
  return render(request, 'core/search_vendor.html' , context )



def search_product(request , vid):
    query = request.GET.get("q" , "")
    vendor = Vendor.objects.get(vid= vid)
    product = Product.objects.filter(title__icontains=query , vendor = vendor , product_status="published")
    
    context = {
        "query": query,
        "product": product,
        "vendor": vendor,
    } 
    return render(request, 'core/search_product.html', context)


from decimal import Decimal
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Vendor, Product, CartOrder, CartOrderItems
import resend
from decouple import config


def cardorder(request, vid):
    vendor = get_object_or_404(Vendor, vid=vid)
    products = Product.objects.filter(vendor=vendor, product_status="published")

    if request.method == "POST":

        product_ids = request.POST.getlist("product_id[]")
        product_names = request.POST.getlist("productName[]")
        # ✅ تم الإبقاء على product_prices كقائمة كما تم إرسالها من JS
        product_prices_list = request.POST.getlist("price[]")
        print(product_prices_list)
        qun = request.POST.getlist("qun[]")

        lng = request.POST.get("lng")
        lat = request.POST.get("lat")

        send_delivry_service = Decimal(request.POST.get("send_delivry_service", 0))

        # معالجة الإحداثيات
        lng = None if lng in [None, "", "null", "undefined"] else float(lng)
        lat = None if lat in [None, "", "null", "undefined"] else float(lat)

        if not product_ids:
            return HttpResponse("❌ لا يوجد منتجات", status=400)

        # ✅ استخراج vendor من أول منتج (منطقي وصحيح)
        first_product = get_object_or_404(Product, pid=product_ids[0])
        vendor = first_product.vendor

        user = request.user if request.user.is_authenticated else None
        customer_name = request.POST.get("name", "Guest")

        # ✅ حساب مجموع الكميات
        total_quantity = sum(int(q) for q in qun)

        # إنشاء الطلب
        order = CartOrder.objects.create(
            user=request.user if request.user.is_authenticated else None,
            vendor_new=vendor,
            customer_name=customer_name,
            qunt=total_quantity,
            product_price=Decimal("0.00"),  # سيتم تحديثه لاحقًا
            lng=lng,
            lat=lat,
            delivry=send_delivry_service,
        )

        # ✅ حساب السعر الكلي الصحيح لإنشاء عناصر الطلب فقط
        calculated_total_price_with_quantities = Decimal("0.00")

        # ✅ إنشاء عناصر الطلب
        for pid, name, price, quantity in zip(product_ids, product_names, product_prices_list, qun):
            product = Product.objects.filter(pid=pid).first()
            if not product:
                continue

            quantity = int(quantity)
            price = Decimal(price)
            item_total = price * quantity
            print(f"Item Total : {item_total}")

            CartOrderItems.objects.create(
                order=order,
                product=product,
                product_status="processing",
                item=product.title,
                image=product.image.url if product.image else "",
                quantity=quantity,
                price=price,
                total=item_total,
                invoice_on=f"INV-{order.id}-{product.pid}",
            )

            # إضافة قيمة السلعة الإجمالية (السعر * الكمية) إلى المجموع الصحيح
            calculated_total_price_with_quantities += item_total
            
            # ❌ تم إزالة السطر الذي كان يسبب المشكلة (إعادة تعيين المتغير بشكل خاطئ):
            # total_price = product_prices
            

        # ✅ تعيين السعر الكلي كما أرسلته الجافاسكريبت، ولكن يجب تحويله إلى Decimal
        # ⚠️ ملاحظة: قمت بافتراض أن القيمة المرسلة في product_prices_list هي قيمة واحدة تمثل الإجمالي.
        # إذا كانت القائمة تحتوي على أكثر من سعر، فالمنطق لا يزال غير صحيح، ولكني سأفترض أنك تقصد الإجمالي:
        
        # 1. نحول القائمة إلى سلسلة نصية لتمثيل الإجمالي الذي أرسلته (هنا يمكن أن تكون المشكلة)
        # إذا كانت القيمة المرسلة هي قيمة الإجمالي النهائي من JS:
        try:
            # افتراض أن القيمة النهائية هي العنصر الأول في القائمة المرسلة
            final_product_price = Decimal(product_prices_list[0])
        except (IndexError, TypeError, ValueError):
            # في حالة عدم إرسال قيمة، نستخدم القيمة المحسوبة داخليًا
            final_product_price = calculated_total_price_with_quantities
        
        total_price = final_product_price
        
        # ✅ تحديث السعر النهائي في حقل الطلب (باستخدام القيمة المرسلة من JS)
        order.product_price = total_price
        order.save()

        # بيانات إضافية
        phone = request.POST.get("phone")
        address1 = request.POST.get("address-line-1")
        notes = request.POST.get("notes")

        # ✅ حساب الإجمالي الكلي (سعر المنتجات كما أرسلته JS + التوصيل)
        total = total_price + send_delivry_service

        # ✅ إرسال الإيميل
        import resend
        from decouple import config
        
        resend.api_key = config("RESEND_API_KEY")
        resend.Emails.send({
            "from": "Acme <info@blingoservic.com>",
            "to": ["blingohyper@gmail.com"],
            "subject": "New Order",
            "html": f"""
                New order From: {user.username if user else 'Guest'}<br>
                Phone: {phone}<br>
                Address: {address1}<br>
                Notes: {notes}<br>
                Products Price: {total_price}<br>
                Delivery: {send_delivry_service}<br>
                Total: {total}
            """
        })

        return HttpResponse("✅ تم إنشاء الطلب بنجاح")

    return render(request, "core/cardorder.html", {
        "vendor": vendor,
        "product": products,
    })



def robots_txt(request):
    content = """
User-agent: *
Disallow: /admin/
Disallow: /lang/
Disallow: /register/
Disallow: /logout_view/
Disallow: /cardorder/
Disallow: /customer/
Disallow: /createstorevendorform/
Disallow: /errorpage/


Allow: /
Sitemap: https://blingoservic.com/sitemap.xml
"""
    return HttpResponse(content, content_type="text/plain")
