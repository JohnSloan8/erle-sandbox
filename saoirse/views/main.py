from django.shortcuts import render
from django.conf import settings
from .speech_synthesis.utils.text_to_speech import voices
import json

# Create your views here.
def saoirse(request):

    sorted_voices = sorted([*voices])
    in_development = settings.DEBUG
    context = {
        'voices': sorted_voices,
        'in_development': json.dumps(in_development)
    }

    return render(request, 'saoirse/main.html', context)
