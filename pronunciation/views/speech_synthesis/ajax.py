from django.views.decorators.csrf import csrf_exempt
from pronunciation.models import AudioFile, AudioAlteration
from django.http import JsonResponse
from pronunciation.views.speech_synthesis.utils.text_to_speech import create_synthesis
from pronunciation.views.speech_recognition.utils.modify_audio import create_new_audio_file
from pronunciation.views.speech_recognition.utils.speech_to_text import get_audio_length
import json
import code
import os
from django.conf import settings
import time

@csrf_exempt
def store_typed_transcript_correction(request):

    time.sleep(3)
    # print('request.GET:', request.GET)
    # code.interact(local=locals())
    data = json.loads(request.GET['JSONData'])
    
    indexes = data['indexesToBeDeleted']
    integers_start_finish = data['integersStartFinish']
    transcript = data['transcript']
    relative_filename = data['relativeFilename']
    audio_id = data['ID']
    audio_count = data['count'] + 1
    typed_string = data['typedString']
    temp_synth_relative_filename = create_synthesis(typed_string)

    a = AudioFile.objects.get(pk=audio_id)
    a_a = AudioAlteration(audio_file=a)
    a_a.relative_filename, a_a.updated_words = create_new_audio_file(indexes, transcript, relative_filename, audio_count, deletion=False, temp_synth_relative_filename_=temp_synth_relative_filename, typed_string_=typed_string, integers_start_finish_=integers_start_finish)
    a_a.save()

    updated_duration = get_audio_length(os.path.join(settings.BASE_DIR, 'media', a_a.relative_filename))

    response_data = {
        'updated_relative_filename': a_a.relative_filename,
        'updated_words': a_a.updated_words,
        'updated_duration': updated_duration,
        'updated_audio_count': audio_count,

    }

    return JsonResponse(response_data)    

