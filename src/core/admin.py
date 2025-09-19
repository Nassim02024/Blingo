from django.contrib import admin
from django.contrib.auth.models import User
from core.models import Product , CartOrder , Vendor , CartOrderItems , Category , Imgs_product , ProductReview , Wishlist , Address
# Register your models here.
 

class ProductImagesAdmin(admin.TabularInline):
  model = Imgs_product
  
  
# from model.py class product line 79
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImagesAdmin]
    list_display = [
        "pid", "user", "title", "product_image", "price",
        "old_price", "color", "description", "featured", "product_status"
    ]

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        try:
            vendor = Vendor.objects.get(user=request.user)
            return qs.filter(vendor=vendor)
        except Vendor.DoesNotExist:
            return qs.none()

    def get_readonly_fields(self, request, obj=None):
        # نخليهم للعرض فقط وقت التعديل
        if obj:  
            return ["user", "vendor"]
        return []  # وقت الإضافة يخليهم editable حتى يتعبّو تلقائي

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if not obj:  # يعني وقت إضافة منتج جديد
            form.base_fields["user"].initial = request.user
            try:
                vendor = Vendor.objects.get(user=request.user)
                form.base_fields["vendor"].initial = vendor
            except Vendor.DoesNotExist:
                pass
        return form

    def save_model(self, request, obj, form, change):
        if not obj.user:
            obj.user = request.user
        if not obj.vendor:
            try:
                obj.vendor = Vendor.objects.get(user=request.user)
            except Vendor.DoesNotExist:
                obj.vendor = None
        super().save_model(request, obj, form, change)

  

  
# from model.py class category line 36
class CategoryAdmin(admin.ModelAdmin):
  list_display = ["cid", "categoress" , "Category_imge"] 
  # readonly_fields = ["cid" ,"categoress" , "Category_imge"]
  
  
# from model.py class vendor line 52
class VendorAdmin(admin.ModelAdmin):
  list_display = ["vid" , "title" , "image"]
  
  

# from model.py class cardOrderItems line 141
class CartOrderItemsAdmin(admin.StackedInline):
  model = CartOrderItems
  extra = 0  # مهم حتى لا تظهر صفوف إضافية فارغة

  
  # from model.py class cartOrder line 129 
class CartOrderAdmin(admin.ModelAdmin):
    model = CartOrder
    inlines = [CartOrderItemsAdmin]
    list_display = ["id", "product_name", "product_price", "user", "fullname", "email", "customer_name", "paid_status", "order_date", "product_status"]

  
  
  
class CartOrderItemsMainAdmin(admin.ModelAdmin):
  list_display = ["order", "invoice_on", "item", "image", "quantity", "price", "total"]

  
  
  
  
  
# from model.py class cardOrder line 164
class ProductReviewAdmin(admin.ModelAdmin):
  list_display = ["user" , "product" , "review" , "rating"]




# from model.py class cardOrder line 184
class WishlistAdmin(admin.ModelAdmin):
  list_display = ["user" , "product" , "date"]
  
  
  
# from model.py class cardOrder line 197
class AddressAdmin(admin.ModelAdmin):
  list_display = ["user" , "address" , "status"]



admin.site.register(Product , ProductAdmin)
admin.site.register(Category , CategoryAdmin)
admin.site.register(Vendor , VendorAdmin)
admin.site.register(CartOrder , CartOrderAdmin)
admin.site.register(CartOrderItems, CartOrderItemsMainAdmin)
admin.site.register(ProductReview , ProductReviewAdmin)
admin.site.register(Wishlist , WishlistAdmin)
admin.site.register(Address , AddressAdmin)