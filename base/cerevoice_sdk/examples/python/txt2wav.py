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
import os
import sys
import platform

PLATFORM = platform.system()
IS_PYTHON3 = sys.version_info[0] >= 3
IS_64BIT = sys.maxsize > 2**32

# Add CereVoice Engine to the path
sdkdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
PYLIBDIR = 'py3lib' if IS_PYTHON3 else 'pylib'
if IS_64BIT and PLATFORM == "Windows":
    PYLIBDIR += '64'
engdir = os.path.join(sdkdir, 'cerevoice_eng', PYLIBDIR)
print('sdkdir:', sdkdir)
sys.path.append(engdir)
import time

#
# Cereproc imports
#
import cerevoice_eng


def parse_arguments():
    from optparse import OptionParser

    # Default input/output directory
    cwd = os.getcwd()

    # Setup option parsing
    usage="""%prog [options] -v voice_file -l license_file -r root_certificate_file
                            -c certificate_file -k certificate_key
                            -i infile1 [-i infile2...]

Synthesise an xml or text file to a wav file and transcription."""

    parser = OptionParser(usage=usage)
    parser.add_option("-v", "--voice_file", help="Path to voice file")
    parser.add_option("-l", "--license_file",help="CereProc license file", default="")
    parser.add_option("-r", "--root_certificate_file", help="Root CA certificate file to connect with license server", default="")
    parser.add_option("-c", "--certificate_file", help="Certificate file to connect with license server", default="")
    parser.add_option("-k", "--certificate_key_file", help="Certificate key to connect with license server", default="")
    parser.add_option("-i", "--input_file", dest='inputs', action='append', help="Input file to be synthesised")
    parser.add_option("-o", "--outdir", dest="outdir", default=cwd, help="Output directory, defaults to {}".format(cwd))
    parser.add_option("-d", "--ondisk", dest="ondisk", action="store_true", help="Load keeping audio and index data on disk")

    opts, args = parser.parse_args()

    # Check correct info supplied. A license file can be provided with
    # no certificate files.  Alternatively certificates can be
    # provided with or without a license file.
    if not opts.voice_file:
        parser.error("a voice file must be supplied")
    if not opts.inputs:
        parser.error("one or more input files must be provided")
    if not os.access(opts.voice_file, os.R_OK):
        parser.error("can't access voice file '%s'" % opts.voice_file)
    if (not opts.root_certificate_file or not opts.certificate_file or not opts.certificate_key_file) \
       and not os.access(opts.license_file, os.R_OK):
        parser.error("can't access license file '%s' (required if all certificates are not provided)" % opts.license_file)
    if opts.root_certificate_file and not os.access(opts.root_certificate_file, os.R_OK):
        parser.error("can't access root CA certificate file '%s'" % opts.root_certificate_file)
    if opts.certificate_file and not os.access(opts.certificate_file, os.R_OK):
        parser.error("can't access client certificate file '%s'" % opts.certificate_file)
    if opts.certificate_key_file and not os.access(opts.certificate_key_file, os.R_OK):
        parser.error("can't access client certificate key file '%s'" % opts.certificate_key_file)
    if opts.outdir:
        if not os.access(opts.outdir, os.W_OK):
            parser.error("can't write to output directory output directory '%s'" % opts.outdir)

    return opts

def main():
    print('\n----start----\n')
    opts = parse_arguments()

    # Create an engine
    time_engine_0 = time.time()
    engine = cerevoice_eng.CPRCEN_engine_new()
    time_engine_1 = time.time()
    print('engine creation: ', time_engine_1 - time_engine_0)

    # Set the loading mode - all data to RAM or with audio and indexes on disk
    time_load_0 = time.time()
    loadmode = cerevoice_eng.CPRC_VOICE_LOAD
    if opts.ondisk:
        loadmode = cerevoice_eng.CPRC_VOICE_LOAD_EMB
        print('on disk')

    # Load the voice
    ret = cerevoice_eng.CPRCEN_engine_load_voice(engine, opts.voice_file.encode('utf-8'),
                                                 b"", loadmode,
                                                 opts.license_file.encode('utf-8'),
                                                 opts.root_certificate_file.encode('utf-8'),
                                                 opts.certificate_file.encode('utf-8'),
                                                 opts.certificate_key_file.encode('utf-8'))
    
    time_load_1 = time.time()
    print('load voice: ', time_load_1 - time_load_0)

    time_info_0 = time.time()
    if not ret:
        sys.stderr.write("ERROR: could not load the voice, check your license verification files integrity\n")
        sys.exit(1)
    # Get some information about the first loaded voice (index 0)
    name = cerevoice_eng.CPRCEN_engine_get_voice_info(engine, 0, b"VOICE_NAME")
    srate = int(cerevoice_eng.CPRCEN_engine_get_voice_info(engine, 0, b"SAMPLE_RATE"))
    sys.stderr.write("INFO: voice name is '%s', sample rate '%s'\n" % (name.decode('utf-8'), srate))
    time_info_1 = time.time()
    print('get info: ', time_info_1 - time_info_0)

    # Process the input files
    for f in opts.inputs:
        time_process_0 = time.time()
        print('opts.inputs:', opts.inputs)
        indata = open(f).read()
        # Synthesise to a file
        wavout = os.path.join(opts.outdir, os.path.basename(os.path.splitext(f)[0])) + ".wav"
        cerevoice_eng.CPRCEN_engine_speak_to_file(engine, indata.encode('utf-8'), wavout.encode('utf-8'))
        sys.stderr.write("INFO: wrote wav file '%s'\n" % wavout)
        time_process_1 = time.time()
        print('process: ', time_process_1 - time_process_0)

    # Clean up
    cerevoice_eng.CPRCEN_engine_delete(engine)

if __name__ == '__main__':
    main()
