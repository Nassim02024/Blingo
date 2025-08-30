from django.shortcuts import render , redirect
from .forms import UserStoreForm
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
      form = UserStoreForm(request.POST)
      if form.is_valid():
        store = form.save(commit=False)
        store.owner = request.user  # ✅ هنا كان خطأ: request.User => الصحيح request.user
        store.save()
        messages.success(request, "تم إنشاء المتجر بنجاح! انتظر موافقة عليه")
        send_mail(
          subject="New Store Created",
          from_email=request.user.email,
          message=f"New store created by {store.owner.username} \nName:{store.name} \nPhone:{store.phone_number} \nAddress:{store.address} \nPlease review it.",
          recipient_list=['blingohyper@gmail.com']
        )
        if  store.owner.is_vendor == True:          
          store.owner.save() 
          messages.success(request, " تم إنشاء المتجر بنجاح! يمكنك انشاء منتجاتك الان")
          return redirect('index')
        
        return redirect('index')  # أو أي صفحة تريد الانتقال إليها بعد إنشاء المتجر
      else:
        messages.error( request , 'Errore')
        return render(request , "'createstorevendorform/createstorevendorform.html'")
    except Exception as e:
      messages.error(request, f"حدث خطأ أثناء إنشاء المتجر: {str(e)}")
      return redirect('index')
    
  else:
    form = UserStoreForm()
            
  context = {
    'form': form
  }
  return render(request, 'createstorevendorform/createstorevendorform.html' , context )


      
      
