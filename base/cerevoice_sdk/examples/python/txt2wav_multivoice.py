#!/usr/bin/env python

# Copyright (c) 2011-2016 CereProc Ltd.
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
import os
import sys
import platform

PLATFORM = platform.system()
IS_PYTHON3 = sys.version_info[0] >= 3
IS_64BIT = sys.maxsize > 2**32

# Add CereVoice Engine to the path
sdkdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
envdir = os.environ.get('CPRC_BUILD_DIR', "")
if envdir:
    sdkdir = envdir
PYLIBDIR = 'py3lib' if IS_PYTHON3 else 'pylib'
if IS_64BIT and PLATFORM == "Windows":
    PYLIBDIR += '64'
engdir = os.path.join(sdkdir, 'cerevoice_eng', PYLIBDIR)
sys.path.insert(0, engdir)

#
# Cereproc imports
#
import cerevoice_eng

def parse_arguments():
    from argparse import ArgumentParser

    # Default input/output directory
    cwd = os.getcwd()

    # Setup option parsing
    usage="""%%prog [options] -v voice_file -l license_file -r root_certificate_file
                            -c certificate_file -k certificate_key
                            -i infile1 [-i infile2...]

Synthesise an xml or text file to a wav file and transcription."""

    parser = ArgumentParser()
    parser.add_argument("-v", "--voice_file", default = [], action = 'append',
                        help="Path to voice file can be specified multiple times to load additional voices")
    parser.add_argument("-l", "--license_file", default = [], action = 'append',
                        help="CereProc license file, can be specified multiple times for addtional licsences")
    parser.add_argument("-r", "--root_certificate_file", help="Root CA certificate file to connect with license server", default="")
    parser.add_argument("-c", "--certificate_file", help="Certificate file to connect with license server", default="")
    parser.add_argument("-k", "--certificate_key_file", help="Certificate key to connect with license server", default="")
    parser.add_argument("-i", "--input_file", dest='inputs', action='append', help="Input file to be synthesised")
    parser.add_argument("-o", "--outdir", dest="outdir", default=cwd, help="Output directory, defaults to {}".format(cwd))
    parser.add_argument("-d", "--ondisk", dest="ondisk", action="store_true", help="Load keeping audio and index data on disk")

    parser.add_argument("--no-encode-strings", action = "store_true",
                        help = "do not decode the strings")

    opts = parser.parse_args()

    # Check correct info supplied. A license file can be provided with
    # no certificate files.  Alternatively certificates can be
    # provided with or without a license file.
    if not opts.voice_file:
        parser.error("at least 1 voice file must be supplied")
    if not opts.inputs:
        parser.error("one or more input files must be provided")
    for voicefn in opts.voice_file:
        if not os.access(voicefn, os.R_OK):
            parser.error("can't access voice file '%s'" % voicefn)
    if (not opts.root_certificate_file or not opts.certificate_file or not opts.certificate_key_file) \
       and not any([os.access(l, os.R_OK) for l in opts.license_file]):
        parser.error("can't access license file '%s' (required if all certificates are not provided)" % opts.license_file[0])
    if opts.root_certificate_file and not os.access(opts.root_certificate_file, os.R_OK):
        parser.error("can't access root CA certificate file '%s'" % opts.root_certificate_file)
    if opts.certificate_file and not os.access(opts.certificate_file, os.R_OK):
        parser.error("can't access client certificate file '%s'" % opts.certificate_file)
    if opts.certificate_key_file and not os.access(opts.certificate_key_file, os.R_OK):
        parser.error("can't access client certificate key file '%s'" % opts.certificate_key_file)
    if opts.outdir:
        if not os.access(opts.outdir, os.W_OK):
            parser.error("can't write to output directory output directory '%s'" % opts.outdir)

    if not opts.license_file:
        opts.license_file = ['']


    return opts


class Certs:
    def __init__(self, opts):
        if opts.no_encode_strings:
            self.root_cert = opts.root_certificate_file
            self.cert_file = opts.certificate_file
            self.cert_key = opts.certificate_key_file
        else:
            self.root_cert = opts.root_certificate_file.encode('utf-8')
            self.cert_file = opts.certificate_file.encode('utf-8')
            self.cert_key = opts.certificate_key_file.encode('utf-8')

def load_voices(engine, loadmode, opts):
    # Load the voicelicense
    certs = Certs(opts)
    for voice in opts.voice_file:
        configstr = "" if opts.no_encode_strings else b""
        vce = voice if opts.no_encode_strings else voice.encode('utf-8')
        vce_loaded = False
        for license in opts.license_file:
            lic = license if opts.no_encode_strings else license.encode('utf-8')
            ret = cerevoice_eng.CPRCEN_engine_load_voice(engine, vce, configstr, loadmode, lic, certs.root_cert, certs.cert_file, certs.cert_key)
            if ret:
                vce_loaded = True
                sys.stderr.write("INFO: loaded {0}\n".format(voice))
                break
        if not vce_loaded:
            sys.stderr.write("ERROR: could not load the voice file {0}, check your license verification files integrity\n".format(voice))
            sys.exit(1)

    for i in range(cerevoice_eng.CPRCEN_engine_get_voice_count(engine)):
        name, srate = voice_info(engine, opts, i)
        sys.stderr.write("INFO: voice {0} name is '{1}', sample rate '{2}'\n".format(i, name, srate))
    

def voice_info(engine, opts, i):
    name_key = "VOICE_NAME" if opts.no_encode_strings else b"VOICE_NAME"
    srate_key = "SAMPLE_RATE" if opts.no_encode_strings else b"SAMPLE_RATE"
    name = cerevoice_eng.CPRCEN_engine_get_voice_info(engine, i, name_key)
    if type(name) == bytes:
        name = name.decode('utf8')
    srate = int(cerevoice_eng.CPRCEN_engine_get_voice_info(engine, i, srate_key))
    return name, srate

def main():
    opts = parse_arguments()

    # Create an engine
    engine = cerevoice_eng.CPRCEN_engine_new()

    # Set the loading mode - all data to RAM or with audio and indexes on disk
    loadmode = cerevoice_eng.CPRC_VOICE_LOAD
    if opts.ondisk:
        loadmode = cerevoice_eng.CPRC_VOICE_LOAD_EMB

    # Load the voice
    load_voices(engine, loadmode, opts)

    # Get some information about the first last voice (index 0)
    name, srate = voice_info(engine, opts, cerevoice_eng.CPRCEN_engine_get_voice_count(engine)-1)
    sys.stderr.write("\nINFO: default voice name is '{0}', sample rate '{1}'\n".format(name, srate))

    # Process the input files
    for f in opts.inputs:
        indata = open(f).read()
        # Synthesise to a file
        wavout = os.path.join(opts.outdir, os.path.basename(os.path.splitext(f)[0])) + ".wav"
        eng_wavout = wavout
        if not opts.no_encode_strings:
            indata = indata.encode('utf-8')
            eng_wavout = wavout.encode('utf-8')
        cerevoice_eng.CPRCEN_engine_speak_to_file(engine, indata, eng_wavout)
        sys.stderr.write("INFO: wrote wav file '%s'\n" % wavout)

    # Clean up
    cerevoice_eng.CPRCEN_engine_delete(engine)

if __name__ == '__main__':
    main()
