from scipy.io import wavfile
import ffmpeg
import os
import shutil
from django.conf import settings
# import subprocess
from google.cloud import speech_v1
import io
import code

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/john/johnsHDD/PhD/2018_autumn/erle-3666ad7eec71.json"
client = speech_v1.SpeechClient()
language_code = "en-US"
sample_rate_hertz = 22050
config = {
    "enable_word_time_offsets": True,
    "language_code": language_code,
    "model": "phone_call",
    "use_enhanced": True,
}

def get_speech_recognition(aud_file):

    # convert from .webm to wav for Google's speech-to-text using a Python ffmpeg package
    input_aud_loc = os.path.join(settings.BASE_DIR, 'media', 'recorded_speech',  aud_file)
    output_aud_loc = os.path.join(settings.BASE_DIR, 'media', 'recorded_speech', 'wav', aud_file + '_00.' + settings.AUDIO_EXTENSION)
    output_aud_loc_mp3 = os.path.join(settings.BASE_DIR, 'media', 'recorded_speech', 'mp3', aud_file)

    transcript = ''
    words = []
    try:
        ffmpeg.input(input_aud_loc).output(output_aud_loc, ar=16000).run()
        with io.open(output_aud_loc, "rb") as f:
            content = f.read()

        audio = { "content": content }

        response = client.recognize(config, audio)

        for r in response.results:
            for w in r.alternatives[0].words:
                clean_word = w.word.replace('.', '').replace(',', '')
                if clean_word != "":
                    transcript += clean_word + ' '
                    # print('\n\nw:', w)
                    words.append({'word': clean_word, 'voice': True, 'start_time': w.start_time.seconds + float('0.' +  str(w.start_time.nanos)), 'end_time': w.end_time.seconds + float('0.' +  str(w.end_time.nanos))})
                    # print('words:', words)
        transcript = transcript.strip()

        duration = get_audio_length(output_aud_loc)
        print('duration:', duration)

    except Exception as e:
        print("\n\nFFMPEG Error\n\n")
        print("Exception: ", e)

    # cant use this cause my ffmpeg messes up, but need it for iphone later
    # try:
        # ffmpeg.input(input_aud_loc).output(output_aud_loc_mp3, audio_bitrate='32k').run()
    # except:
        # print('ffmpeg error in making mp3')
    
    shutil.copy( input_aud_loc, output_aud_loc_mp3 )

    return [transcript, words, duration]

def get_audio_length(wav_path):
    try:
        samplingFrequency, signalData = wavfile.read(wav_path)
        return (int((len(signalData)/samplingFrequency)*1000))/1000
    except:
        logger.error('\n\nerror from get_audio_length:' + str(e) + '\n')
        return 0
