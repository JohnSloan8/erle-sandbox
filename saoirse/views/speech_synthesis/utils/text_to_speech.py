from saoirse.models import SynthesisedSpeech
from suds.client import Client
from urllib.request import Request, urlopen
from django.conf import settings
import json
import os

accountID = 'placeholder'
password = 'placeholder'
try:
    accountID = settings.CEREPROC_ACC_ID
    password = settings.CEREPROC_PASSWORD
except:
    pass

soapclient = Client("https://cerevoice.com/soap/soap_1_1.php?WSDL")

# print(soapclient.service.listVoices( accountID, password ));

vocal_gesture_dict = {
    'haha': ['g0001_021', 'g0001_022', 'g0001_023', 'g0001_024'],
    'umm': ['g0001_015', 'g0001_016'],
    'err': ['g0001_017', 'g0001_018'],
    'hehe': ['g0001_019', 'g0001_020'],
    'argh': ['g0001_032', 'g0001_033'],
    'hmm': ['g0001_014'],
    'gasp': ['g0001_052'],
}

viseme_gesture_dict = {
    'haha': [{"name": "haha", "start": 800, "end": 800, "Viseme": "happy", "stress": "0"}, {"name": "haha", "start": 0, "end": 0, "Viseme": "happy", "stress": "0"}],
    'umm': [{"name": "umm", "start": 1000, "end": 1000, "Viseme": "b", "stress": "0"}, {"name": "laugh", "umm": 0, "end": 0, "Viseme": "b", "stress": "0"}],
    'err': [{"name": "err", "start": 800, "end": 800, "Viseme": "r", "stress": "0"}, {"name": "laugh", "err": 0, "end": 0, "Viseme": "r", "stress": "0"}],
    'hehe': [{"name": "hehe", "start": 800, "end": 800, "Viseme": "happy", "stress": "0"}, {"name": "hehe", "start": 0, "end": 0, "Viseme": "happy", "stress": "0"}],
    'argh': [{"name": "argh", "start": 800, "end": 800, "Viseme": "disgust", "stress": "0"}, {"name": "argh", "start": 0, "end": 0, "Viseme": "disgust", "stress": "0"}],
    'hmm': [{"name": "hmm", "start": 800, "end": 800, "Viseme": "b", "stress": "0"}, {"name": "hmm", "start": 0, "end": 0, "Viseme": "b", "stress": "0"}],
    'gasp': [{"name": "gasp", "start": 800, "end": 800, "Viseme": "surprise", "stress": "0"}, {"name": "gasp", "start": 0, "end": 0, "Viseme": "surprise", "stress": "0"}],
}

dic = {
    '0': "SIL",
    '1': 'e',
    '2': 'e',
    '3': 'e',
    '4': 'e',
    '5': 'r',
    '6': 'e',
    '7': 'u',
    '8': 'e',
    '9': 'e',
    '10': 'e',
    '11': 'e',
    '12': 'e',
    '13': 'r',
    '14': 'l',
    '15': 's',
    '16': 's',
    '17': 'th',
    '18': 'f',
    '19': 't',
    '20': 'k',
    '21': 'b',
    "w":"w"
}

def create_vocal_gesture( gesture_text ):

    return "<spurt audio='" + random.choice(vocal_gesture_dict[gesture_text]) + "'>laugh</spurt> "

def create_speech_synthesis_object( text, pitch, emotion, accent, initial_delay=500 ):

    s_s = SynthesisedSpeech(text=text, pitch=pitch, voice=accent, emotion=emotion)
    name = accent + '-' + emotion + '-' + str(pitch) + '-' + text.replace(' ', '_').replace('?', '')
    split_text = text.split()

    gesture = None
    first_word = split_text[0]
    to_be_spoken = "" 
    if first_word in [*vocal_gesture_dict]:
        second_word_on = " ".join(split_text[1:])
        gesture = first_word
        to_be_spoken = create_vocal_gesture( first_word ) + "<break time='800ms'/>" + second_word_on
        first_word = split_text[1]
    else:
        to_be_spoken = " ".join(split_text)
    
    emotion if emotion != 'neutral' else ''
    ssml = "<voice emotion='" + emotion + "'>" + to_be_spoken + "</voice>"
    url, visemes = create_tia_tts_url(first_word, gesture, ssml, 'synthesisedSpeech', name, initial_delay, pitch, accent)

    s_s.visemes = json.dumps(visemes)
    s_s.url = url
    s_s.save()
    
    return s_s

voices = {
    'Irish': 'Caitlin-CereWave',
    'Scottish-1': 'Heather-CereWave',
    'Dutch': 'Ada-CereWave',
    'English-RP-1': 'Amy-CereWave',
    'Mexican': 'Ana-CereWave',
    'Russian': 'Avrora-CereWave',
    'USA-East-Coast-1': 'Carolyn-CereWave',
    'Scottish-Mid-Minch': 'Ceitidh-CereWave',
    'Romanian': 'Daria-CereWave',
    'Canadian-French': 'Florence-CereWave',
    'German': 'Gudrun-CereWave',
    'USA-East-Coast-2': 'Hannah-CereWave',
    'USA-East-Coast-3': 'Isabella-CereWave',
    'English-RP-2': 'Jess-CereWave',
    'USA-East-Coast-4': 'Katherine-CereWave',
    'Scottish-2': 'Kirsty-CereWave',
    'Italian': 'Laura-CereWave',
    'English-RP-3': 'Lauren-CereWave',
    'Portuguese': 'Lucia-CereWave',
    'Chinese': 'Mailin-CereWave',
    'USA-West-Coast-1': 'Megan-CereWave',
    'French': 'Nicole-CereWave',
    'Irish-Ulster': 'Peig-CereWave',
    'Polish': 'Pola-CereWave',
    'Catalan-1': 'Rita-CereWave',
    'Catalan-2': 'Sara-CereWave',
    'English-RP-4': 'Sarah-CereWave',
    'French-Metropolitan': 'Suzanne-CereWave',
    'Swedish': 'Ylva-CereWave',
    'Japanese': 'Yuki-CereWave'

}
def create_tia_tts_url(first_word, gesture, text, directory, filename, initial_delay, pitch, accent):

    pitch_for_request = str(0.75 + (pitch / 200))
    voice = voices[accent]


    ssml_text = '<s><break time="' + str(initial_delay) + 'ms"/><prosody pitch="' + str(pitch_for_request) + '" >' + text + '</prosody></s>'

    request = soapclient.service.speakExtended(accountID, password, voice, ssml_text, 'mp3', 22050, False, True)
    print('request: ', request)
    viseme_data = get_viseme_data(first_word, request.metadataUrl)
    if gesture != None:
        first_two_visemes = viseme_gesture_dict[gesture]
        first_two_visemes[1]['start'] = viseme_data[1]["end"] - 600
        first_two_visemes[1]['end'] = viseme_data[1]["end"] - 800
        viseme_data = first_two_visemes + viseme_data

    url = create_url( request.fileUrl, directory, filename )

    return url, viseme_data

def create_url(url, directory, name):

    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    file_url = os.path.join( directory, name + '.mp3' )
    final_file_url = os.path.join(settings.MEDIA_ROOT, file_url)
    with urlopen(req) as response:
        with open(final_file_url, 'wb') as output:
            output.write(response.read())

    return file_url


def get_viseme_data(first_word, metadataUrl):
    xml = get_xml_from_url(metadataUrl)
    parsed_xml = parse_xml(first_word, xml)
    return parsed_xml

def get_xml_from_url(metadataUrl):
    data = []
    with urlopen(metadataUrl) as response:
        data = [line.decode('utf-8') for line in response]
    return data

def parse_xml(first_word, xml):

    rid_of_unwanted_beginning = []
    after_first_word = False
    gesture = False
    for line in xml:
        if after_first_word:
            if '<phone' in line and '<phone name="sil"' not in line:
                rid_of_unwanted_beginning.append(line)
        else:
            if "CPRC_GESTURE_START" in line:
                gesture = True
            elif "CPRC_GESTURE_END" in line:
                gesture = False
            if not gesture:
                if '<phone' in line and '<phone name="sil"' not in line:
                    rid_of_unwanted_beginning.append(line)
                    after_first_word = True


    out = []
    for r in rid_of_unwanted_beginning:
        temp = {}
        for w in r[6:-3].split():
            s = w.split("=")
            name = ""
            if s[0] not in ['disney_viseme', 'sapi_viseme']:
                if s[0] == 'name':
                    name = s[1][1:-1]
                if s[0] in ['start','end']:
                    temp[s[0]] = round(float(s[1][1:-1])*1000)
                else:
                    temp[s[0]] = s[1][1:-1]
            if s[0] == 'sapi_viseme':
                if name == 'w':
                    code = 'w'
                else:
                    code = s[1][1:-1]
                try:
                    temp['Viseme'] = dic[code]
                except:
                    temp['Viseme'] = dic['0']
        # if temp['Viseme'] != "SIL":
        temp['Viseme'] += 'Temp'
        out.append(temp)
    return out

