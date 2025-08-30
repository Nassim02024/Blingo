from django.shortcuts import render
from django.shortcuts import redirect

from django.utils.translation import gettext as _
from django.utils.translation import get_language , activate 
from django.utils import translation

def lang(request, language):
    # activate('ar')
    translation.activate(language)
    request.session[translation.LANGUAGE_SESSION_KEY] = language
    return redirect(request.META.get("HTTP_REFERER", "/"))

