from base.cerevoice_sdk.examples.python.tts_callback import main as tts_local_main

def create_synthesis(phrase):

    ssml_text = "<s>" + phrase + "</s>"
    filename = phrase.replace(' ', '')

    url = 'synthesisedSpeech/tmp/' + filename + '.wav'

    raw_viseme_list = tts_local_main( ssml_text, url )    
    print('\n\nssml_text:', ssml_text)
    print('url:', url, '\n\n')

    # viseme_list = clean_viseme_data(raw_viseme_list)
    return url #, raw_viseme_list

# def clean_viseme_data(viseme_data):

    # rid_of_unwanted_beginning = []
    # after_first_word = False
    # gesture = False
    # for line in viseme_data:
        # if after_first_word:
            # if line['type'] == 'phoneme' and line['Viseme'] != 'sil':
                # try:
                    # line['Viseme'] = phone_dic[line['Viseme']]
                # except KeyError:
                    # line['Viseme'] = 'e'
                # rid_of_unwanted_beginning.append(line)
        # else:
            # if line['Viseme'] == "CPRC_GESTURE_START":
                # gesture = True
            # elif line['Viseme'] == "CPRC_GESTURE_END":
                # gesture = False
            # if not gesture:
                # if line['type'] == 'phoneme' and line['Viseme'] != 'sil':
                    # try:
                        # line['Viseme'] = phone_dic[line['Viseme']]
                    # except KeyError:
                        # line['Viseme'] = 'e'
                    # rid_of_unwanted_beginning.append(line)
                    # after_first_word = True

    # return rid_of_unwanted_beginning
