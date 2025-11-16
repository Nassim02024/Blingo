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

 
def createstorevendorform(request):

  if request.method == 'POST':
    try:
      form = creatvendor(request.POST , request.FILES)
      if form.is_valid():
        store = form.save(commit=False)
        store.user = request.user  
        store.save()
        messages.success(request, "تم إنشاء المتجر بنجاح! انتظر موافقة عليه")

        contact = request.POST.get("contact")
        address = request.POST.get("address")
        title = request.POST.get("title")
        days_to_return = request.POST.get("days_to_return")
        image = request.POST.get("image")

        resend.api_key = config("RESEND_API_KEY")
        params: resend.Emails.SendParams = {
            "from": "Acme <info@blingoservic.com>",
            "to": ["blingohyper@gmail.com"],
            "subject": "hello world",
            "html": f"New Store create from: {request.user.username}<br>store name: {title}<br>address: {address}<br>day to return: {days_to_return}<br>contact: {contact} <br> هل توافق على انشاء المنتجر",
        }
        email = resend.Emails.send(params)
        print(email)
        
        if  store.owner.is_vendor == True:          
          store.owner.save() 
          messages.success(request, " تم إنشاء المتجر بنجاح! يمكنك انشاء منتجاتك الان")
          return redirect('index')
        
        return redirect('index')  # أو أي صفحة تريد الانتقال إليها بعد إنشاء المتجر
      else:
        print(form.errors)  # هذا سيظهر لك سبب عدم صلاحية الفورم
        messages.error(request, 'Errore')

        return render(request , "createstorevendorform/createstorevendorform.html")
    except Exception as e:
      messages.error(request, f"حدث خطأ أثناء إنشاء المتجر: {str(e)}")
      return redirect('index')
    
  else:
    form = creatvendor()
            
  context = {
    'form': form
  }
  return render(request, 'createstorevendorform/createstorevendorform.html' , context )


      
      
