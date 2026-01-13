from decouple import config
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
import resend
from django.contrib.auth import get_user_model
from core.models import Vendor # تأكد من استيراد Vendor من المكان الصحيح
from .forms import creatvendor
from .models import UserStore # تأكد من استيراد UserStore من المكان الصحيح (إذا كان في نفس التطبيق)

User = get_user_model()


def createstorevendorform(request):
    # تحقق من أن المستخدم مسجل الدخول
    if not request.user.is_authenticated:
        messages.error(request, "يجب تسجيل الدخول لإنشاء متجر.")
        return redirect('login') # أو اسم دالة تسجيل الدخول

    if request.method == 'POST':
        form = creatvendor(request.POST, request.FILES)
        
        if form.is_valid():
            try:
                # 1. حفظ المتجر وربطه بالمستخدم الحالي في جدول UserStore
                store = form.save(commit=False)
                store.user = request.user
                store.save()  # حفظ سجل المتجر الأول (UserStore)
                
                # 2. تعيين حالة المستخدم كبائع 'قيد الانتظار'
                # إذا لم يكن الحقل موجودًا في نموذج المستخدم، يجب إزالته أو إضافته
                request.user.is_vendor = False # الوضع الافتراضي أو 'قيد المراجعة'
                request.user.save()

                # 3. إنشاء سجل في جدول Vendor
                # نستخدم البيانات التي تم حفظها للتو في store
                
                # ✅ حماية حقل الصورة: قد لا يكون موجودًا أو قد يحتاج إلى طريقة وصول مختلفة
                image_val = getattr(store, 'image', None) 
                if image_val and hasattr(image_val, 'name'):
                    image_val = image_val.name # إذا كان الحقل من نوع CloudinaryField أو ImageField

                # يتم إنشاء سجل Vendor هنا، أو جلب الموجود إذا كان قد تم إنشاؤه مسبقًا
                Vendor.objects.get_or_create(
                    user=request.user,
                    defaults={
                        'title': store.title,
                        'image': image_val, # استخدام قيمة الصورة المتاحة
                        'description': getattr(store, 'description', ''),
                        'address': getattr(store, 'address', 'No Address'),
                        'contact': getattr(store, 'contact', 'No Contact'),
                        # يمكنك إضافة حقل is_approved أو status لتعيين حالة المتجر "قيد المراجعة"
                    }
                )
                
                # 4. كود إرسال الإيميل عبر Resend (كما هو)
                try:
                    resend.api_key = config("RESEND_API_KEY")
                    params = {
                        "from": "Acme <info@blingoservic.com>",
                        "to": ["blingohyper@gmail.com"],
                        "subject": f"متجر جديد بانتظار المراجعة: {store.title}",
                        "html": f"""
                            <h3>تم إنشاء متجر جديد وبانتظار الموافقة</h3>
                            <b>المستخدم:</b> {request.user.username}<br>
                            <b>اسم المتجر:</b> {store.title}<br>
                            <b>العنوان:</b> {getattr(store, 'address', 'N/A')}<br>
                            <b>رقم الهاتف:</b> {getattr(store, 'contact', 'N/A')}<br>
                            <p>يرجى الدخول إلى لوحة الإدارة لمراجعة المتجر وتفعيل حالة is_vendor للمستخدم إذا تمت الموافقة.</p>
                        """,
                    }
                    resend.Emails.send(params)
                except Exception as e:
                    print(f"Email sending failed: {e}")
                
                # 5. رسالة نجاح
                messages.success(request, "✅ تم إرسال طلب إنشاء المتجر بنجاح! حاليا لايمكنك اضافة المنتجات انتظر الموافقة وستظهر لك خانة لوحة القيادة .")
                return redirect('index') # وجهه إلى الصفحة الرئيسية أو صفحة الانتظار

            except Exception as e:
                # ✅ عرض الخطأ بوضوح للمطور في Console
                print(f"An unexpected error occurred during store creation: {e}")
                messages.error(request, "❌ حدث خطأ غير متوقع أثناء إنشاء المتجر. يرجى المحاولة لاحقًا.")
                return redirect('index') 
        
        else:
            # إذا لم يكن الفورم صالحاً
            print("Form errors:", form.errors)
            messages.error(request, "يوجد خطأ في البيانات المدخلة، يرجى المحاولة مرة أخرى.")
            # إرجاع الفورم مع الأخطاء إلى نفس القالب
            return render(request, "createstorevendorform/createstorevendorform.html", {'form': form})
    
    else:
        # في حالة طلب الصفحة (GET)
        form = creatvendor()
        context = {'form': form}
        return render(request, 'createstorevendorform/createstorevendorform.html', context)