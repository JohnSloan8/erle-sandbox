#!/usr/bin/env python

# Copyright (c) 2015-2019 CereProc Ltd.
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
# This is an example program to produce audio output with synchronised
# events using the CereVoice Engine API.
#

#
# Standard imports
#
from __future__ import print_function
import os
import sys
import platform
import time
import threading

# Determine current platform and OS architecture to import correct libraries
PLATFORM = platform.system()
IS_PYTHON3 = sys.version_info[0] >= 3
IS_64BIT = sys.maxsize > 2**32

if IS_PYTHON3:
    import queue as Queue
else:
    import Queue

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

# Threaded audio queue processing
class AudioThread(threading.Thread):
    def __init__(self, player, audioqueue):
        self.srate = cerevoice_aud.CPRC_sc_player_sample_rate(player)
        self.player = player
        self.audioqueue = audioqueue
        threading.Thread.__init__ (self)

    def run(self):
        while 1:
            buf, events = self.audioqueue.get()
            if not buf:
                return
            
            # Play the audio in the audio player thread
            cerevoice_aud.CPRC_sc_audio_play(self.player, buf)
            
            # Fire events
            for sleep, msg in events:
                cerevoice_aud.CPRC_sc_sleep_msecs(sleep)
                # Note that we could resync using data from the audio
                # player, if required (this function is a total, not
                # phrase-based) e.g.:
                # nsamples = cerevoice_aud.CPRC_sc_player_samples_sent(self.player)
                print(msg)

            # Wait until finished, then clean up
            while cerevoice_aud.CPRC_sc_audio_busy(self.player):
                cerevoice_aud.CPRC_sc_sleep_msecs(10)
            cerevoice_aud.CPRC_sc_audio_delete(buf)


# User data class to store information we would like to have
# access to in the callback.
class EngineUserData:
    def __init__(self, engine, channel, audioqueue):
        # Audio queue
        self.audioqueue = audioqueue
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

    # The callback function must be called 'channel_callback'
    def channel_callback(self, data):
        # Get the audio buffer for this piece of synthesis output
        abuf = cerevoice_eng.data_to_abuf(data)
        prevstart = 0.0
        events = []
        trans_mk = cerevoice_eng.CPRC_abuf_trans_mk(abuf)
        trans_done = cerevoice_eng.CPRC_abuf_trans_done(abuf)
        for i in range(trans_mk, trans_done + 1):
            trans = cerevoice_eng.CPRC_abuf_get_trans(abuf, i)
            start = cerevoice_eng.CPRC_abuf_trans_start(trans)
            name = cerevoice_eng.CPRC_abuf_trans_name(trans)
            if cerevoice_eng.CPRC_abuf_trans_type(trans) == cerevoice_eng.CPRC_ABUF_TRANS_PHONE:
                events.append((int((start-prevstart)*1000), "INFO: phoneme\t'%s'" % name))
            elif cerevoice_eng.CPRC_abuf_trans_type(trans) == cerevoice_eng.CPRC_ABUF_TRANS_WORD:
                events.append((int((start-prevstart)*1000), "INFO: word\t'%s'" % name))
            elif cerevoice_eng.CPRC_abuf_trans_type(trans) == cerevoice_eng.CPRC_ABUF_TRANS_MARK:
                events.append((int((start-prevstart)*1000), "INFO: mark\t'%s'" % name))
            else:
                print("WARNING: transcription type '%s' not known" % cerevoice_eng.CPRC_abuf_trans_type(trans))
            prevstart = start

        # Create an audio buffer for playing - this structure must
        # be deleted after it has been played.
        wav_mk = cerevoice_eng.CPRC_abuf_wav_mk(abuf)
        wav_added = cerevoice_eng.CPRC_abuf_added_wav_sz(abuf)
        abuf_done = cerevoice_eng.CPRC_abuf_extract(abuf, wav_mk, wav_added)
        buf = cerevoice_aud.CPRC_sc_audio_short(cerevoice_eng.CPRC_abuf_wav_data(abuf_done),
                                                cerevoice_eng.CPRC_abuf_wav_sz(abuf_done))
        cerevoice_eng.CPRC_abuf_delete(abuf_done)

        # Send data to the audio playback queue
        self.userdata.audioqueue.put((buf, events))
        
        # Example of resetting the channel from within the callback.
        # After a reset the callback will no longer fire, and
        # synthesis will stop.
        #cerevoice_eng.CPRCEN_engine_channel_reset(self.userdata.engine, self.userdata.channel)


def parse_arguments():
    from optparse import OptionParser

    # Default input/output directory
    cwd = os.getcwd()

    # Setup option parsing
    usage="""%prog [options] -v voice_file -l license_file -r root_certificate_file
                             -c certificate_file -k certificate_key_file
                             -i infile1 [-i infile2...]

Synthesise an xml/text file, firing events during playback"""

    parser = OptionParser(usage=usage)
    parser.add_option("-v", "--voice_file",
                        help="Path to voice file")
    parser.add_option("-l", "--license_file", default = "",
                        help="CereProc license file")
    parser.add_option("-r", "--root_certificate_file", default = "",
                        help="Root CA certificate file to connect with license server")
    parser.add_option("-c", "--certificate_file", default = "",
                        help="Certificate file to connect with license server")
    parser.add_option("-k", "--certificate_key_file", default = "",
                        help="Certificate key to connect with license server")
    parser.add_option("-i", "--input_file", dest='inputs', action='append',
                        help="Input file to be synthesised")
    parser.add_option("-d", "--ondisk", action="store_true",
                        help="Load keeping audio and index data on disk")
    opts, args = parser.parse_args()

    # Check correct info supplied
    if opts.license_file:
        if not os.access(opts.license_file, os.R_OK):
            parser.error("can't access license file '%s'" % opts.license_file)
    elif opts.root_certificate_file and opts.certificate_file and opts.certificate_key_file:
        if not os.access(opts.root_certificate_file, os.R_OK):
            parser.error("can't access root CA certificate file '%s'" % opts.root_certificate_file)
        if not os.access(opts.certificate_file, os.R_OK):
            parser.error("can't access client certificate file '%s'" % opts.certificate_file)
        if not os.access(opts.certificate_key_file, os.R_OK):
            parser.error("can't access client certificate key file '%s'" % opts.certificate_key_file)
    else:
        parser.error("not enough arguments for license verification provided")
    
    if not opts.voice_file:
        parser.error("a voice file must be supplied")
    if not opts.inputs:
        parser.error("one or more input files must be provided")
    if not os.access(opts.voice_file, os.R_OK):
        parser.error("can't access voice file '%s'" % opts.voice_file)

    return opts

def main():
    opts = parse_arguments()

    # Create an engine
    engine = cerevoice_eng.CPRCEN_engine_new()

    # Set the loading mode - all data to RAM or with audio and indexes on disk
    loadmode = cerevoice_eng.CPRC_VOICE_LOAD
    if opts.ondisk:
        loadmode = cerevoice_eng.CPRC_VOICE_LOAD_EMB

    # Load the voice
    ret = cerevoice_eng.CPRCEN_engine_load_voice(engine,  opts.voice_file.encode('utf-8'),
                                                 b"", cerevoice_eng.CPRC_VOICE_LOAD_EMB, opts.license_file.encode('utf-8'),
                                                 opts.root_certificate_file.encode('utf-8'),
                                                 opts.certificate_file.encode('utf-8'),
                                                 opts.certificate_key_file.encode('utf-8'))
    if not ret:
        sys.stderr.write("ERROR: could not load the voice, check license verification files integrity\n")
        sys.exit(1)
    info = cerevoice_eng.CPRCEN_engine_get_voice_info(engine, 0, b"VOICE_NAME")
    srate = int(cerevoice_eng.CPRCEN_engine_get_voice_info(engine, 0, b"SAMPLE_RATE"))
    sys.stderr.write("INFO: voice name is '%s', sample rate '%s'\n" % (info.decode('utf-8'), srate))
    player = cerevoice_aud.CPRC_sc_player_new(srate)

    # Queue for audio and event processing
    audioqueue = Queue.Queue(maxsize=5)
    # Thread for audio and event processing
    audiothread = AudioThread(player, audioqueue)
    audiothread.start()
    # Process the input files
    for f in opts.inputs:
        indata = open(f).read()
        channel = cerevoice_eng.CPRCEN_engine_open_default_channel(engine)
        userdata = EngineUserData(engine, channel, audioqueue)
        cc = CereVoiceEngineCallback(userdata)
        res = cerevoice_eng.engine_set_callback(engine, channel, cc)
        if res:
            print("INFO: callback set successfully")
            cerevoice_eng.CPRCEN_engine_channel_speak(engine, channel, indata.encode('utf-8'), len(indata.encode('utf-8')), 1)
        else:
            sys.stderr.write("ERROR: could not set callback, synthesis data cannot be processed")

    # Send empty data to audio queue to trigger exit
    audioqueue.put(("", ""))
    audiothread.join()
    # Clean up
    cerevoice_eng.CPRCEN_engine_delete(engine)

if __name__ == '__main__':
    main()
