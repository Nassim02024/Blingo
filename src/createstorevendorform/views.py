from decouple import config
from django.shortcuts import render , redirect
import resend
from .forms import creatvendor
from django.contrib.auth import get_user_model 
from users.models import User
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from .models import UserStore

User = get_user_model()

 
from django.shortcuts import render, redirect
from django.contrib import messages
import resend
from decouple import config
from core.models import Vendor  # تأكد من استيراد موديل Vendor

def createstorevendorform(request):
    if request.method == 'POST':
        try:
            form = creatvendor(request.POST, request.FILES)
            if form.is_valid():
                # 1. حفظ المتجر وربطه بالمستخدم الحالي
                store = form.save(commit=False)
                store.user = request.user
                store.save()  # يتم إنشاء ID المتجر هنا (مثلاً رقم 16)

                # 2. تحديث حالة المستخدم ليصبح بائعاً في نظام Django
                request.user.is_vendor = True
                request.user.save()

                # 3. إنشاء سجل في جدول Vendor (هام جداً لحل IntegrityError)
                # هذا السطر يضمن أن رقم البائع (ID) موجود في جداول العلاقات
                Vendor.objects.get_or_create(
                    user=request.user,
                    defaults={
                        'title': store.title,
                        'image': store.image,
                        'description': getattr(store, 'description', ''),
                        'address': getattr(store, 'address', 'No Address'),
                        'contact': getattr(store, 'contact', 'No Contact'),
                    }
                )

                # 4. كود إرسال الإيميل عبر Resend
                try:
                    resend.api_key = config("RESEND_API_KEY")
                    params = {
                        "from": "Acme <info@blingoservic.com>",
                        "to": ["blingohyper@gmail.com"],
                        "subject": f"متجر جديد: {store.title}",
                        "html": f"""
                            <h3>تم إنشاء متجر جديد</h3>
                            <b>المستخدم:</b> {request.user.username}<br>
                            <b>اسم المتجر:</b> {store.title}<br>
                            <b>العنوان:</b> {getattr(store, 'address', 'N/A')}<br>
                            <b>رقم الهاتف:</b> {getattr(store, 'contact', 'N/A')}
                        """,
                    }
                    resend.Emails.send(params)
                except Exception as e:
                    print(f"Email sending failed: {e}")

                messages.success(request, "تم إنشاء المتجر بنجاح! يمكنك الآن إضافة منتجاتك.")
                return redirect('index')
            
            else:
                # إذا لم يكن الفورم صالحاً
                print(form.errors)
                messages.error(request, "يوجد خطأ في البيانات المدخلة، يرجى المحاولة مرة أخرى.")
                return render(request, "createstorevendorform/createstorevendorform.html", {'form': form})

        except Exception as e:
            messages.error(request, f"حدث خطأ أثناء إنشاء المتجر: {str(e)}")
            return redirect('index')
    
    else:
        # في حالة طلب الصفحة (GET)
        form = creatvendor()
            
    context = {'form': form}
    return render(request, 'createstorevendorform/createstorevendorform.html', context)

      
      
