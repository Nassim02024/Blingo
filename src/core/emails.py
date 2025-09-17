from decouple import config
from django.http import HttpResponse
import resend

# نقرأ المفتاح من متغير البيئة
resend.api_key = config("RESEND_API_KEY")

def send_email_with_resend(to_email, subject, text):
    """
    دالة لإرسال إيميل باستخدام Resend
    """
    return resend.Emails.send({
        "from": "info@blingoservic.com",  # استبدل بدومينك المؤكد
        "to": [to_email],
        "subject": subject,
        "text": text
    })
   