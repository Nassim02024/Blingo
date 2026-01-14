# import time
# import requests
# import hashlib
# from django.conf import settings

# def send_purchase_event(request, order):
#     url = f"https://graph.facebook.com/v18.0/{settings.META_PIXEL_ID}/events"

#     payload = {
#         "data": [
#             {
#                 "event_name": "Purchase",
#                 "event_time": int(time.time()),
#                 "event_id": str(order.id),  # مهم لـ Deduplication
#                 "action_source": "website",
#                 "event_source_url": request.build_absolute_uri(),
#                 "user_data": {
#                     "client_ip_address": request.META.get('REMOTE_ADDR'),
#                     "client_user_agent": request.META.get('HTTP_USER_AGENT'),
#                     "em": hashlib.sha256(
#                         order.email.lower().encode()
#                     ).hexdigest()
#                 },
#                 "custom_data": {
#                     "currency": "DZD",
#                     "value": float(order.total)
#                 }
#             }
#         ]
#     }

#     requests.post(url, params={
#         "access_token": settings.META_ACCESS_TOKEN
#     }, json=payload)
