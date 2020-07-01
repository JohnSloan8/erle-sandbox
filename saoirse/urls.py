from django.urls import path
from saoirse.views import main
from saoirse.views.speech_synthesis import ajax

urlpatterns = [
    path('', main.saoirse, name='saoirse'),
    path('get_speech_synthesis', ajax.get_speech_synthesis, name='get_speech_synthesis'),
]

# if settings.DEBUG:
    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
