from scipy.io import wavfile
import numpy as np
from django.conf import settings
from pronunciation.views.speech_recognition.utils.speech_to_text import get_audio_length
import os

def create_new_audio_file(indexes_, transcript_, relative_filename_, audio_count_, deletion=True, temp_synth_relative_filename_='', typed_string_='', integers_start_finish_=[]):

    blank_insertion = False
    if len(indexes_) == 0:
        blank_insertion = True
        blank_integer = int(integers_start_finish_[0])
        print('blank_integer:', blank_integer)
        if blank_integer == 0:
            after_blank_index = 0
            before_blank_index = 0
            start_delete = 0
            end_delete = transcript_[0]['start_time']
        else:
            after_blank_index = int(blank_integer / 2)
            before_blank_index = after_blank_index - 1
            print('before_blank_index:', before_blank_index)
            print('after_blank_index:', after_blank_index)
            print('transcript:', transcript_)
            start_delete = transcript_[before_blank_index]['end_time']
            if after_blank_index >= len(transcript_):
                end_delete = start_delete
            else:
                end_delete = transcript_[after_blank_index]['start_time']
    else:
        start_index = indexes_[0]
        end_index = indexes_[len(indexes_) - 1]    
        start_delete = transcript_[start_index]['start_time']
        end_delete = transcript_[end_index]['end_time']

    absolute_filename = os.path.join(settings.BASE_DIR, 'media', relative_filename_)
    rate, data = wavfile.read(absolute_filename)

    duration_synth = 0
    data_synth = []
    if not deletion:
        absolute_synth_filename = os.path.join(settings.BASE_DIR, 'media', temp_synth_relative_filename_)
        rate_synth, data_synth = wavfile.read(absolute_synth_filename)
        duration_synth = get_audio_length(absolute_synth_filename)

    split_0 = int(rate * start_delete)
    split_1 = int(rate * end_delete)

    left_data, right_data = data[:split_0-1], data[split_1:]

    if not blank_insertion:
        if indexes_[0] == 0:
            if deletion:
                combined = right_data
            else:
                combined = np.concatenate((data_synth, right_data))
        elif indexes_[len(indexes_) - 1] == len(transcript_) - 1:
            if deletion:
                combined = left_data
            else:
                combined = np.concatenate(( left_data, data_synth ))
        else:
            if deletion:
                combined = np.concatenate(( left_data, right_data ))
            else:
                combined = np.concatenate((left_data, data_synth, right_data))
    else:
        if integers_start_finish_[0] == 0:
            combined = np.concatenate((data_synth, right_data))
        else:
            combined = np.concatenate((left_data, data_synth, right_data))
    string_audio_count = str(audio_count_)
    if len(string_audio_count) == 1:
        string_audio_count = '0' + string_audio_count
    
    updated_relative_filename = relative_filename_[:-6] + string_audio_count + '.' + settings.AUDIO_EXTENSION
    updated_absolute_filename = os.path.join(settings.BASE_DIR, 'media', updated_relative_filename )
    print('combined:', combined)
    wavfile.write(updated_absolute_filename, rate, combined)

    # create new transcript without deleted word and modified timestamps
    duration_to_be_changed = 0
    if not blank_insertion:
        if start_index == 0:
            if deletion:
                duration_to_be_changed = -end_delete
            else:
                duration_to_be_changed = -end_delete + duration_synth
        else:
            duration_to_be_changed = -end_delete + start_delete + duration_synth
    else:
        duration_to_be_changed = -end_delete + start_delete + duration_synth

    for word in transcript_:
        if word['voice'] == False:
            word['voice'] = None

    if blank_insertion:
        left_word_list = transcript_[:after_blank_index]
        right_word_list = transcript_[after_blank_index:]
    else:
        left_word_list = transcript_[:start_index]
        right_word_list = transcript_[end_index + 1:]

    synth_word_list = []
    if not deletion:
        word_list = typed_string_.split()
        cumulative_time = 0
        no_words = len(word_list)
        time_per_word = duration_synth / no_words
        for w in word_list:
            synth_word_list.append({'word': w, 'voice': False, 'start_time': start_delete + cumulative_time, 'end_time': start_delete + cumulative_time + time_per_word })
            cumulative_time += time_per_word

    updated_timesptamps_right_word_list = []
    for w in right_word_list:
        w['start_time'] += duration_to_be_changed
        w['end_time'] += duration_to_be_changed
        updated_timesptamps_right_word_list.append(w)

    updated_words = left_word_list + synth_word_list + updated_timesptamps_right_word_list
    # print('updated_words:', updated_words)

    return updated_relative_filename, updated_words

