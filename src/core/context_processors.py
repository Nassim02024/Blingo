from django.shortcuts import get_object_or_404
from django.urls import resolve
from core.models import User, Product, CartOrder, Vendor, CartOrderItems, Category, Imgs_product, ProductReview, Wishlist, Address

def default(request):
    # محاولة الحصول على vid من URL
    vendor = None
    categories = []
    
    try:
        resolver_match = resolve(request.path_info)
        vid = resolver_match.kwargs.get('vid')  # استخراج vid من الرابط

        if vid:
            vendor = get_object_or_404(Vendor, vid=vid)
            categories = Category.objects.filter(vendor=vendor)
        else:
            categories = Category.objects.none()
    except Exception:
        categories = Category.objects.none()
    
    return {
        "categorys": categories,
        "user": request.user,
        "vendor": vendor,
        "product": Product.objects.all(),
    }
