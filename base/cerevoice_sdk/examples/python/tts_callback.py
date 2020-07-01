#!/usr/bin/env python

# Copyright (c) 2011-2019 CereProc Ltd.
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

#
# This is a simple program to produce audio output using the CereVoice
# Engine API.
#

#
# Standard imports
#
from __future__ import print_function
import os
import sys
import platform
import json
from django.conf import settings

PLATFORM = platform.system()
IS_PYTHON3 = sys.version_info[0] >= 3
IS_64BIT = sys.maxsize > 2**32

# Add CereVoice Engine to the path
sdkdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
PYLIBDIR = 'py3lib' if IS_PYTHON3 else 'pylib'
if IS_64BIT and PLATFORM == "Windows":
    PYLIBDIR += '64'
engdir = os.path.join(sdkdir, 'cerevoice_eng', PYLIBDIR)
auddir = os.path.join(sdkdir, 'cerevoice_aud', PYLIBDIR)
sys.path.append(engdir)
sys.path.append(auddir)

#
# Cereproc imports
#
import cerevoice_eng
import cerevoice_aud

# User data class to store information we would like to have
# access to in the callback.
class EngineUserData:
    def __init__(self, wavout, engine, channel, player):
        # If false, audio is being played
        self.wavout = wavout
        # Audio player
        self.player = player
        # These two are optional, they can be used to control
        # cancellation in the callback function.
        self.engine = engine
        self.channel = channel

# Channel event callback function
class CereVoiceEngineCallback:
    def __init__(self, userdata):
        # User-configurable parameter, could be as simple as a file
        # name for the output, or a richer data structure.
        self.userdata = userdata
        self.phoneme_list = []

    # The callback function must be called 'channel_callback'
    def channel_callback(self, data):
        cumulative_time_for_break = 0
        # Get the audio buffer for this piece of synthesis output
        abuf = cerevoice_eng.data_to_abuf(data)
        # Print transcription information from the audio buffer
        # This information could be used for lip syncing, markers
        # can be used to send data to this application via the
        # engine.
        trans_mk = cerevoice_eng.CPRC_abuf_trans_mk(abuf)
        trans_done = cerevoice_eng.CPRC_abuf_trans_done(abuf)
        for i in range(trans_mk, trans_done + 1):
            trans = cerevoice_eng.CPRC_abuf_get_trans(abuf, i)
            if trans:
                start = int(cerevoice_eng.CPRC_abuf_trans_start(trans) * 1000)
                end = int(cerevoice_eng.CPRC_abuf_trans_end(trans) * 1000)
                name = cerevoice_eng.CPRC_abuf_trans_name(trans).decode('utf-8')
                if len(self.phoneme_list) != 0 and start == 0.0:
                    cumulative_time_for_break = self.phoneme_list[-1]["end"]
                self.phoneme_list.append({"Viseme": name, "start": start + cumulative_time_for_break, "end": end + cumulative_time_for_break})
                if cerevoice_eng.CPRC_abuf_trans_type(trans) == cerevoice_eng.CPRC_ABUF_TRANS_PHONE:
                    # print("INFO: phoneme '%s', start '%s', end '%s'" % (name, start, end))
                    self.phoneme_list[-1]['type'] = 'phoneme'
                elif cerevoice_eng.CPRC_abuf_trans_type(trans) == cerevoice_eng.CPRC_ABUF_TRANS_WORD:
                    # print("INFO: word '%s', start '%s', end '%s'" % (name, start, end))
                    self.phoneme_list[-1]['type'] = 'word'
                elif cerevoice_eng.CPRC_abuf_trans_type(trans) == cerevoice_eng.CPRC_ABUF_TRANS_MARK:
                    # print("INFO: marker '%s', start '%s', end '%s'" % (name, start, end))
                    self.phoneme_list[-1]['type'] = 'marker'
                else:
                    # print("WARNING: transcription type '%s' not known" % cerevoice_eng.CPRC_abuf_trans_type(trans))
                    self.phoneme_list[-1]['type'] = 'unknown'
        # print('phoneme_list:', phoneme_list)

        # If pipelining is on, we may have partial audio returned in
        # the callback. Extract the completed audio:
        wav_mk = cerevoice_eng.CPRC_abuf_wav_mk(abuf)
        wav_added = cerevoice_eng.CPRC_abuf_added_wav_sz(abuf)
        abuf_done = cerevoice_eng.CPRC_abuf_extract(abuf, wav_mk, wav_added)

        # Save the output.  Creates a new file on the first call,
        # appends on subsequent calls
        if self.userdata.wavout:
            cerevoice_eng.CPRC_riff_append(abuf_done, self.userdata.wavout.encode('utf-8'))
        else:
            # Cue the audio for playing
            if self.userdata.player:
                buf = cerevoice_aud.CPRC_sc_audio_short_disposable(cerevoice_eng.CPRC_abuf_wav_data(abuf_done),
                                                                   cerevoice_eng.CPRC_abuf_wav_sz(abuf_done))
                cerevoice_aud.CPRC_sc_audio_cue(self.userdata.player, buf)

        cerevoice_eng.CPRC_abuf_delete(abuf_done)

        # Example of resetting the channel from within the callback.
        # After a reset the callback will no longer fire, and
        # synthesis will stop.
        #cerevoice_eng.CPRCEN_engine_channel_reset(self.userdata.engine, self.userdata.channel)

# def parse_arguments():
    # from optparse import OptionParser

    # # Default input/output directory
    # cwd = os.getcwd()

    # # Setup option parsing
    # usage="""%prog [options] -v voice_file -l license_file -r root_certificate_file
                                 # -c certificate_file -k certificate_key
                                 # -i infile1 [-i infile2...]

# Synthesise an xml/text file to a wav file and transcription, or play back the audio."""

    # parser = OptionParser(usage=usage)
    # parser.add_option("-v", "--voice_file", help="Path to voice file")
    # parser.add_option("-l", "--license_file", help="CereProc license file")
    # parser.add_option("-r", "--root_certificate_file", default="", help="Root CA certificate file to connect with license server")
    # parser.add_option("-c", "--certificate_file", default="", help="Certificate file to connect with license server")
    # parser.add_option("-k", "--certificate_key_file", default="", help="Certificate key to connect with license server")
    # parser.add_option("-i", "--inputs", action='append', help="Input file(s) to be synthesised")
    # parser.add_option("-o", "--outdir", default=cwd, help="Output directory, defaults to {}".format(cwd))
    # parser.add_option("-p", "--play", action="store_true", default=False, help="Play back the audio instead of saving, defaults to false")
    # parser.add_option("-P", "--pipe", type="int", help="Pipe length for DNN voices (0 =  do not pipeline)")
    # parser.add_option("-d", "--ondisk", action="store_true", help="Load keeping audio and index data on disk")

    # opts, args = parser.parse_args()

    # # Check correct info supplied. A license file can be provided with
    # # no certificate files.  Alternatively certificates can be
    # # provided with or without a license file.
    # if not opts.voice_file:
        # parser.error("a voice file must be supplied")
    # if not opts.inputs:
        # parser.error("one or more input files must be provided")
    # if not os.access(opts.voice_file, os.R_OK):
        # parser.error("can't access voice file '%s'" % opts.voice_file)
    # if (not opts.root_certificate_file or not opts.certificate_file or not opts.certificate_key_file) \
       # and not os.access(opts.license_file, os.R_OK):
        # parser.error("can't access license file '%s' (required if all certificates are not provided)" % opts.license_file)
    # if opts.root_certificate_file and not os.access(opts.root_certificate_file, os.R_OK):
        # parser.error("can't access root CA certificate file '%s'" % opts.root_certificate_file)
    # if opts.certificate_file and not os.access(opts.certificate_file, os.R_OK):
        # parser.error("can't access client certificate file '%s'" % opts.certificate_file)
    # if opts.certificate_key_file and not os.access(opts.certificate_key_file, os.R_OK):
        # parser.error("can't access client certificate key file '%s'" % opts.certificate_key_file)
    # if opts.outdir:
        # if not os.access(opts.outdir, os.W_OK):
            # parser.error("can't write to output directory output directory '%s'" % opts.outdir)

    # return opts

def main( input_ssml, url ):
    # opts = parse_arguments()
    outdir = os.getcwd()
    this_dirname = os.path.dirname(os.path.realpath(__file__))

    # Create an engine
    engine = cerevoice_eng.CPRCEN_engine_new()

    # Set the loading mode - all data to RAM or with audio and indexes on disk
    loadmode = cerevoice_eng.CPRC_VOICE_LOAD
    # if opts.ondisk:
        # loadmode = cerevoice_eng.CPRC_VOICE_LOAD_EMB

    # Load the voice
    voice = this_dirname + "/cerevoice_Caitlin_16k_standard.voice"
    cert_license = this_dirname + "/caitlin.lic"
    cert_root = this_dirname + "/caitlin.pem"
    cert = this_dirname + "/caitlin.crt"
    cert_key = this_dirname + "/caitlin.key"
    ret = cerevoice_eng.CPRCEN_engine_load_voice(engine, voice.encode('utf-8'),
                                                 b"", loadmode, 
                                                 cert_license.encode('utf-8'),
                                                 cert_root.encode('utf-8'),
                                                 cert.encode('utf-8'),
                                                 cert_key.encode('utf-8'))
    if not ret:
        sys.stderr.write("ERROR: could not load the voice, check the integrity of license verification files\n")
        sys.exit(1)
    name = cerevoice_eng.CPRCEN_engine_get_voice_info(engine, 0, b"VOICE_NAME")
    sample_rate = int(cerevoice_eng.CPRCEN_engine_get_voice_info(engine, 0, b"SAMPLE_RATE"))
    sys.stderr.write("INFO: voice name is '%s', sample rate '%s'\n" % (name.decode('utf-8'), sample_rate))

    # Process the input files
    # for f in opts.inputs:

    # f = "test.txt"
    # indata = open(f).read()

    # Synthesise to a file
    # if opts.play:
        # wavout = False
    # else:
    # wavout = os.path.join(outdir, os.path.basename(os.path.splitext(f)[0])) + ".wav"
    wavout = os.path.join(settings.BASE_DIR, 'media', url)
    if os.path.isfile(wavout):
        # print("INFO: removing previous output file '%s'" % wavout)
        os.remove(wavout)
    channel = cerevoice_eng.CPRCEN_engine_open_default_channel(engine)
    # if opts.pipe is not None: cerevoice_eng.CPRCEN_channel_set_pipe_length(engine, channel, opts.pipe)
    freq = int(cerevoice_eng.CPRCEN_channel_get_voice_info(engine, channel, b"SAMPLE_RATE"))
    # if opts.play:
        # player = cerevoice_aud.CPRC_sc_player_new(freq)
        # userdata = EngineUserData(wavout, engine, channel, player)
    # else:
    userdata = EngineUserData(wavout, engine, channel, False)
    cc = CereVoiceEngineCallback(userdata)
    res = cerevoice_eng.engine_set_callback(engine, channel, cc)
    if res:
        # print("INFO: callback set successfully")
        cerevoice_eng.CPRCEN_engine_channel_speak(engine, channel, input_ssml.encode('utf-8'), len(input_ssml.encode('utf-8')), 1)
        if wavout: print("INFO: wrote wav file '%s'" % wavout)
    else:
        sys.stderr.write("ERROR: could not set callback, synthesis data cannot be processed")

    # if opts.play:
        # while cerevoice_aud.CPRC_sc_audio_busy(player):
            # cerevoice_aud.CPRC_sc_sleep_msecs(50)
        # cerevoice_aud.CPRC_sc_player_delete(player)
    # Clean up
    cerevoice_eng.CPRCEN_engine_delete(engine)
    phone_list_without_sil = []
    for p in cc.phoneme_list:
        # print('p:', p)
        if p['Viseme'] != 'sil':
            phone_list_without_sil.append(p)
    return phone_list_without_sil

if __name__ == '__main__':
    main()
