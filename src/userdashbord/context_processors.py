from core.models import User , Product , CartOrder , Vendor , CartOrderItems , Category , Imgs_product , ProductReview , Wishlist , Address

def default(request):
  categorys = Category.objects.all()
  product = Product.objects.all()
  vendor = Vendor.objects.first()
  cardorder = CartOrder.objects.all()


  return {
    "categorys": categorys,
    "user": request.user,
    "vendor": vendor,  # الآن كائن واحد وليس قائمة
    "product": product,
    "cardorder": cardorder,

  }
