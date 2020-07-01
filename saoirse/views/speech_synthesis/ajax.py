from saoirse.views.speech_synthesis.utils.text_to_speech import create_speech_synthesis_object
from django.http import JsonResponse
import json
import code
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def get_speech_synthesis(request):

    data = json.loads(request.GET['JSONData'])
    print( 'data: ', data )

    s_s = create_speech_synthesis_object( data['text'], data['pitch'], data['emotion'], data['voice'] )

    response_data = {
        'url': s_s.url,
        'visemes': s_s.visemes,
    }

    return JsonResponse(response_data)    

