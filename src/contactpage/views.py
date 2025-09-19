from django.shortcuts import render
from django.core.mail import send_mail
import resend
from decouple import config

def contact(request):
    context = {}
    if request.method == "POST":
        try:
            name = request.POST.get('name')
            phone = request.POST.get('phone')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            messages = request.POST.get('messages')

            message = f"Name: {name}\nPhone: {phone}\nEmail: {email}\n{subject}\nMessages: {messages}"

            resend.api_key = config("RESEND_API_KEY")

            params: resend.Emails.SendParams = {
                "from": "Acme <info@blingoservic.com>",
                "to": ["blingohyper@gmail.com"],
                "subject": "hello world",
                "html": f"<strong>{message}</strong>",
            }

            email = resend.Emails.send(params)
            print("success")
            context ["alert_message"] = "تم ارسال بنجاح"

  

        except Exception as e:
            print(e)  
            
            # return render(request, 'contactpage/contactpage.html', {'error': True})
            
         

    return render(request, 'contactpage/contactpage.html' ,  context)
