from django.urls import path
from pronunciation.views import main
from pronunciation.views.speech_recognition import ajax as s_r_ajax
from pronunciation.views.speech_synthesis import ajax as s_s_ajax

urlpatterns = [
    path('', main.pronunciation, name='pronunciation'),
    path('store_blob', s_r_ajax.store_blob, name='store_blob'),
    path('store_typed_transcript_correction', s_s_ajax.store_typed_transcript_correction, name='store_typed_transcript_correction'),
    path('delete_words', s_r_ajax.delete_words, name='delete_words'),
]
