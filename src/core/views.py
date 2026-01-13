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

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from decimal import Decimal
from .models import Vendor, Product, CartOrder, CartOrderItems
from decouple import config
import resend 

def cardorder(request, vid):
    vendor = get_object_or_404(Vendor, vid=vid)

    if request.method == "POST":

        product_ids = request.POST.getlist("product_id[]")
        product_names = request.POST.getlist("productName[]")
        # ✅ ملاحظة هامة: price_per_item_total هي القيمة الإجمالية للعنصر (السعر * الكمية) كما أرسلها الـ JS
        price_per_item_total_list = request.POST.getlist("price[]") 
        qun = request.POST.getlist("qun[]")

        lng = request.POST.get("lng")
        lat = request.POST.get("lat")
        
        try:
            send_delivry_service = Decimal(request.POST.get("send_delivry_service", '0'))
        except:
            send_delivry_service = Decimal('0.00')

        # معالجة الإحداثيات
        lng = None if lng in [None, "", "null", "undefined"] else float(lng)
        lat = None if lat in [None, "", "null", "undefined"] else float(lat)

        if not product_ids:
            return HttpResponse("❌ لا يوجد منتجات", status=400)

        first_product = get_object_or_404(Product, pid=product_ids[0])
        vendor = first_product.vendor

        user = request.user if request.user.is_authenticated else None
        customer_name = request.POST.get("name", "Guest")
        
        total_quantity = sum(int(q) for q in qun)

        # إنشاء الطلب
        order = CartOrder.objects.create(
            user=user,
            vendor_new=vendor,
            customer_name=customer_name,
            qunt=total_quantity,
            product_price=Decimal("0.00"), 
            lng=lng,
            lat=lat,
            delivry=send_delivry_service,
        )

        # ✅ المتغير الذي سيحتوي على إجمالي سعر المنتجات فقط
        calculated_total_price_with_quantities = Decimal("0.00")

        # إنشاء عناصر الطلب وحساب الإجمالي
        for pid, name, item_total_price_str, quantity_str in zip(product_ids, product_names, price_per_item_total_list, qun):
            product = Product.objects.filter(pid=pid).first()
            if not product:
                continue

            quantity = int(quantity_str)
            
            # 💡 السعر الإجمالي للعنصر كما أرسلته الواجهة الأمامية
            try:
                item_total_price = Decimal(item_total_price_str) 
            except:
                item_total_price = Decimal("0.00")
            
            # ✅ حساب سعر الوحدة الفعلي (Total Price / Quantity)
            # نضمن عدم القسمة على صفر، واستخدام كمية المنتج من قاعدة البيانات كاحتياطي إذا لزم الأمر
            if quantity > 0:
                unit_price = item_total_price / quantity 
            else:
                unit_price = Decimal("0.00")
            
            # ✅ سعر الوحدة هو الآن price، والسعر الإجمالي للعنصر هو item_total_price
            
            CartOrderItems.objects.create(
                order=order,
                product=product,
                product_status="processing",
                item=product.title,
                image=product.image.url if product.image else "",
                quantity=quantity,
                price=unit_price,  # 💡 تم تسجيل سعر الوحدة الآن
                total=item_total_price, # 💡 تم تسجيل الإجمالي للعنصر (السعر * الكمية)
                invoice_on=f"INV-{order.id}-{product.pid}",
            )

            # إضافة قيمة السلعة الإجمالية (السعر * الكمية) إلى المجموع الصحيح
            calculated_total_price_with_quantities += item_total_price
            
        # -------------------------------------------------------------
        # ✅ التعديل الحاسم: تحديث product_price في الطلب بالقيمة المحسوبة
        # -------------------------------------------------------------
        total_products_price = calculated_total_price_with_quantities 
        order.product_price = total_products_price
        order.save()

        # بيانات إضافية
        phone = request.POST.get("phone")
        address1 = request.POST.get("address-line-1")
        notes = request.POST.get("notes")

        # ✅ حساب الإجمالي الكلي (سعر المنتجات كما حسبناه + التوصيل)
        total = total_products_price + send_delivry_service

        # ---------------------------------------------
        # ✅ بناء قائمة HTML للمنتجات في الطلب للإيميل (باستخدام القيم الصحيحة)
        # ---------------------------------------------
        products_html = "<h3>Products Ordered:</h3><ul style='list-style: none; padding: 0;'>"
        order_items = CartOrderItems.objects.filter(order=order)

        for item in order_items:
            products_html += f"""
            <li style='margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 5px;'>
                <strong>{item.item}</strong> (Qty: {item.quantity})<br>
                Price per unit: {item.price}<br>
                Total for item: {item.total}
            </li>
            """
        products_html += "</ul>"
        # ---------------------------------------------

        # ✅ إرسال الإيميل
        try:
            resend.api_key = config("RESEND_API_KEY")
            resend.Emails.send({
                "from": "Acme <info@blingoservic.com>",
                "to": ["blingohyper@gmail.com"],
                "subject": f"New Order #{order.id} from {customer_name}",
                "html": f"""
                    <h2>Order Summary - Order #{order.id}</h2>
                    <hr>
                    New order From: {user.username if user else 'Guest'}<br>
                    Customer Name: {customer_name}<br>
                    Phone: {phone}<br>
                    Address: {address1}<br>
                    Notes: {notes}<br>
                    <hr>
                    
                    {products_html} <hr>
                    
                    Products Price (Subtotal): {total_products_price}<br>
                    Delivery: {send_delivry_service}<br>
                    <strong>Total Amount: {total} Dz</strong>
                """
            })
        except Exception as e:
            print(f"Failed to send email: {e}")

        return HttpResponse("✅ تم إنشاء الطلب بنجاح")

    # نعود فقط لعرض الـ Template
    products = Product.objects.filter(vendor=vendor, product_status="published")
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