from django.shortcuts import render
from django.core.mail import send_mail

def contact(request):
    context = {}
    if request.method == "POST":
        try:
            name = request.POST.get('name')
            phone = request.POST.get('phone')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            messages = request.POST.get('messages')

            message = f"Name: {name}\nPhone: {phone}\nEmail: {email}\nMessages: {messages}"

            send_mail(
                subject="New message from customer in Blingo: " + subject,
                message=message,
                from_email=email,
                recipient_list=['blingohyper@gmail.com'],
            )
            print("success")
            context ["alert_message"] = "تم ارسال بنجاح"

  

        except Exception as e:
            print(e)  
            
            # return render(request, 'contactpage/contactpage.html', {'error': True})
            
         

    return render(request, 'contactpage/contactpage.html' ,  context)
