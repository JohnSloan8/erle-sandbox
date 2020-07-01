from django.shortcuts import render
from django.conf import settings
import json

def pronunciation(request):

    in_development = settings.DEBUG
    context = {
        'in_development': json.dumps(in_development)
    }

    return render(request, 'pronunciation/main.html', context)
