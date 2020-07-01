from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from pronunciation.models import AudioFile, AudioAlteration
from django.http import JsonResponse
from pronunciation.views.speech_recognition.utils.speech_to_text import get_speech_recognition, get_audio_length
from pronunciation.views.speech_recognition.utils.modify_audio import create_new_audio_file
from django.conf import settings
import json
import code
import os
import time

@csrf_exempt
def store_blob(request):
    blob = request.FILES['data']
    filename = timezone.now().strftime('%H-%M-%S')
    blob.name = filename
        
    a = AudioFile(
        audio=blob, 
    )
    a.save()

    if a.audio.size != 0:
        transcript, words, duration = get_speech_recognition(filename)
        a.transcript = transcript
        a.words = json.dumps(words)
        filename += '_00.' + settings.AUDIO_EXTENSION
        a.audio.name = 'recorded_speech/wav/' + filename
        a.save()

    response_data = {
        'words': words,
        'relative_filename': a.audio.name,
        'id': a.id,
        'duration': duration,
    }

    return JsonResponse(response_data)    

@csrf_exempt
def delete_words(request):
    time.sleep(3)
    data = json.loads(request.GET['JSONData'])
    
    indexes = data['indexesToBeDeleted']
    transcript = data['transcript']
    relative_filename = data['relativeFilename']
    audio_id = data['ID']
    audio_count = data['count'] + 1

    a = AudioFile.objects.get(pk=audio_id)
    a_a = AudioAlteration(audio_file=a)
    a_a.relative_filename, a_a.updated_words = create_new_audio_file(indexes, transcript, relative_filename, audio_count)
    a_a.save()

    updated_duration = get_audio_length(os.path.join(settings.BASE_DIR, 'media', a_a.relative_filename))

    response_data = {
        'updated_relative_filename': a_a.relative_filename,
        'updated_words': a_a.updated_words,
        'updated_duration': updated_duration,
        'updated_audio_count': audio_count,
    }

    return JsonResponse(response_data)    










