from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _


urlpatterns = [
  path("i18n/", include("django.conf.urls.i18n"))
]


app_name = "core"


urlpatterns += i18n_patterns (
    path('admin/', admin.site.urls),
    path('users/', include(('users.urls', 'users'), namespace='users')),    
    path('', include('core.urls') , name='core' ),
    path('', include('createstorevendorform.urls') , name='createstorevendorform' ),
    path('', include('userdashbord.urls') , name='userdashbord' ),
    path('', include('commingsoon.urls') , name='commingsoon' ),
    path('', include('customer.urls') , name='customer' ),
    path('', include('aboutus.urls') , name='aboutus' ),
    path('', include('errorpage.urls') , name='errorpage' ),
    path('', include('contactpage.urls') , name='contactpage' ),
    path('', include('lang.urls') , name='lang' ),
    path('', include('servece.urls') , name='servece' ),
    prefix_default_language=False

  )


# Static and media files
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
