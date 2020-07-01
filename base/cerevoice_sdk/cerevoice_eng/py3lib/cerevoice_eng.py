# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.11
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_cerevoice_eng')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_cerevoice_eng')
    _cerevoice_eng = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_cerevoice_eng', [dirname(__file__)])
        except ImportError:
            import _cerevoice_eng
            return _cerevoice_eng
        try:
            _mod = imp.load_module('_cerevoice_eng', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _cerevoice_eng = swig_import_helper()
    del swig_import_helper
else:
    import _cerevoice_eng
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0


def engine_set_callback(eng, chan, pyclass):
    """engine_set_callback(CPRCEN_engine * eng, CPRCEN_channel_handle chan, PyObject * pyclass) -> int"""
    return _cerevoice_eng.engine_set_callback(eng, chan, pyclass)

def engine_set_text_callback(eng, chan, pyinstance):
    """engine_set_text_callback(CPRCEN_engine * eng, CPRCEN_channel_handle chan, PyObject * pyinstance) -> int"""
    return _cerevoice_eng.engine_set_text_callback(eng, chan, pyinstance)

def data_to_abuf(l):
    """data_to_abuf(long l) -> CPRC_abuf *"""
    return _cerevoice_eng.data_to_abuf(l)

def abuf_to_string(abuf):
    """abuf_to_string(CPRC_abuf * abuf) -> PyObject *"""
    return _cerevoice_eng.abuf_to_string(abuf)
class CPRCEN_wav(_object):
    """Proxy of C++ CPRCEN_wav class."""

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CPRCEN_wav, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CPRCEN_wav, name)
    __repr__ = _swig_repr
    __swig_setmethods__["wavdata"] = _cerevoice_eng.CPRCEN_wav_wavdata_set
    __swig_getmethods__["wavdata"] = _cerevoice_eng.CPRCEN_wav_wavdata_get
    if _newclass:
        wavdata = _swig_property(_cerevoice_eng.CPRCEN_wav_wavdata_get, _cerevoice_eng.CPRCEN_wav_wavdata_set)
    __swig_setmethods__["size"] = _cerevoice_eng.CPRCEN_wav_size_set
    __swig_getmethods__["size"] = _cerevoice_eng.CPRCEN_wav_size_get
    if _newclass:
        size = _swig_property(_cerevoice_eng.CPRCEN_wav_size_get, _cerevoice_eng.CPRCEN_wav_size_set)
    __swig_setmethods__["sample_rate"] = _cerevoice_eng.CPRCEN_wav_sample_rate_set
    __swig_getmethods__["sample_rate"] = _cerevoice_eng.CPRCEN_wav_sample_rate_get
    if _newclass:
        sample_rate = _swig_property(_cerevoice_eng.CPRCEN_wav_sample_rate_get, _cerevoice_eng.CPRCEN_wav_sample_rate_set)

    def __init__(self):
        """__init__(CPRCEN_wav self) -> CPRCEN_wav"""
        this = _cerevoice_eng.new_CPRCEN_wav()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _cerevoice_eng.delete_CPRCEN_wav
    __del__ = lambda self: None
CPRCEN_wav_swigregister = _cerevoice_eng.CPRCEN_wav_swigregister
CPRCEN_wav_swigregister(CPRCEN_wav)


def CPRCEN_engine_load(voicef, licensef, root_certf, certf, certkey):
    """CPRCEN_engine_load(char const * voicef, char const * licensef, char const * root_certf, char const * certf, char const * certkey) -> CPRCEN_engine *"""
    return _cerevoice_eng.CPRCEN_engine_load(voicef, licensef, root_certf, certf, certkey)

def CPRCEN_engine_load_config(voicef, voice_configf, licensef, root_certf, certf, certkey):
    """CPRCEN_engine_load_config(char const * voicef, char const * voice_configf, char const * licensef, char const * root_certf, char const * certf, char const * certkey) -> CPRCEN_engine *"""
    return _cerevoice_eng.CPRCEN_engine_load_config(voicef, voice_configf, licensef, root_certf, certf, certkey)

def CPRCEN_engine_delete(eng):
    """CPRCEN_engine_delete(CPRCEN_engine * eng)"""
    return _cerevoice_eng.CPRCEN_engine_delete(eng)

def CPRCEN_engine_speak(eng, text):
    """CPRCEN_engine_speak(CPRCEN_engine * eng, char const * text) -> CPRCEN_wav *"""
    return _cerevoice_eng.CPRCEN_engine_speak(eng, text)

def CPRCEN_engine_speak_to_file(eng, text, fname):
    """CPRCEN_engine_speak_to_file(CPRCEN_engine * eng, char const * text, char const * fname) -> int"""
    return _cerevoice_eng.CPRCEN_engine_speak_to_file(eng, text, fname)

def CPRCEN_engine_clear(eng):
    """CPRCEN_engine_clear(CPRCEN_engine * eng) -> int"""
    return _cerevoice_eng.CPRCEN_engine_clear(eng)
CPRC_VOICE_LOAD = _cerevoice_eng.CPRC_VOICE_LOAD
CPRC_VOICE_LOAD_EMB = _cerevoice_eng.CPRC_VOICE_LOAD_EMB
CPRC_VOICE_LOAD_EMB_AUDIO = _cerevoice_eng.CPRC_VOICE_LOAD_EMB_AUDIO
CPRC_VOICE_LOAD_MEMMAP = _cerevoice_eng.CPRC_VOICE_LOAD_MEMMAP
CPRC_VOICE_LOAD_TP = _cerevoice_eng.CPRC_VOICE_LOAD_TP
CPRCEN_RAW = _cerevoice_eng.CPRCEN_RAW
CPRCEN_RIFF = _cerevoice_eng.CPRCEN_RIFF
CPRCEN_AIFF = _cerevoice_eng.CPRCEN_AIFF
CPRCEN_INTERRUPT_BOUNDARY_PHONE = _cerevoice_eng.CPRCEN_INTERRUPT_BOUNDARY_PHONE
CPRCEN_INTERRUPT_BOUNDARY_WORD = _cerevoice_eng.CPRCEN_INTERRUPT_BOUNDARY_WORD
CPRCEN_INTERRUPT_BOUNDARY_NATURAL = _cerevoice_eng.CPRCEN_INTERRUPT_BOUNDARY_NATURAL
CPRCEN_INTERRUPT_BOUNDARY_DEFAULT = _cerevoice_eng.CPRCEN_INTERRUPT_BOUNDARY_DEFAULT
CPRCEN_INTERRUPT_BOUNDARY_LEGACY_SPURT = _cerevoice_eng.CPRCEN_INTERRUPT_BOUNDARY_LEGACY_SPURT
CPRCEN_INTERRUPT_INTERRUPT_HALT = _cerevoice_eng.CPRCEN_INTERRUPT_INTERRUPT_HALT
CPRCEN_INTERRUPT_INTERRUPT_OVERLAP = _cerevoice_eng.CPRCEN_INTERRUPT_INTERRUPT_OVERLAP
CPRCEN_INTERRUPT_INTERRUPT_POLITE = _cerevoice_eng.CPRCEN_INTERRUPT_INTERRUPT_POLITE
CPRCEN_INTERRUPT_INTERRUPT_ANGRY = _cerevoice_eng.CPRCEN_INTERRUPT_INTERRUPT_ANGRY
CPRCEN_INTERRUPT_INTERRUPT_REPLAN = _cerevoice_eng.CPRCEN_INTERRUPT_INTERRUPT_REPLAN
CPRC_ABUF_TRANS_PHONE = _cerevoice_eng.CPRC_ABUF_TRANS_PHONE
CPRC_ABUF_TRANS_WORD = _cerevoice_eng.CPRC_ABUF_TRANS_WORD
CPRC_ABUF_TRANS_MARK = _cerevoice_eng.CPRC_ABUF_TRANS_MARK
CPRC_ABUF_TRANS_ERROR = _cerevoice_eng.CPRC_ABUF_TRANS_ERROR
CPRC_ABUF_TRANS_TYPES = _cerevoice_eng.CPRC_ABUF_TRANS_TYPES
CPRC_UNDEF = _cerevoice_eng.CPRC_UNDEF
CPRC_NUC = _cerevoice_eng.CPRC_NUC
CPRC_ONSET = _cerevoice_eng.CPRC_ONSET
CPRC_CODA = _cerevoice_eng.CPRC_CODA
CPRC_SYLB = _cerevoice_eng.CPRC_SYLB
class CPRC_abuf_trans(_object):
    """Proxy of C++ CPRC_abuf_trans class."""

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CPRC_abuf_trans, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CPRC_abuf_trans, name)
    __repr__ = _swig_repr
    __swig_setmethods__["name"] = _cerevoice_eng.CPRC_abuf_trans_name_set
    __swig_getmethods__["name"] = _cerevoice_eng.CPRC_abuf_trans_name_get
    if _newclass:
        name = _swig_property(_cerevoice_eng.CPRC_abuf_trans_name_get, _cerevoice_eng.CPRC_abuf_trans_name_set)
    __swig_setmethods__["type"] = _cerevoice_eng.CPRC_abuf_trans_type_set
    __swig_getmethods__["type"] = _cerevoice_eng.CPRC_abuf_trans_type_get
    if _newclass:
        type = _swig_property(_cerevoice_eng.CPRC_abuf_trans_type_get, _cerevoice_eng.CPRC_abuf_trans_type_set)
    __swig_setmethods__["start"] = _cerevoice_eng.CPRC_abuf_trans_start_set
    __swig_getmethods__["start"] = _cerevoice_eng.CPRC_abuf_trans_start_get
    if _newclass:
        start = _swig_property(_cerevoice_eng.CPRC_abuf_trans_start_get, _cerevoice_eng.CPRC_abuf_trans_start_set)
    __swig_setmethods__["end"] = _cerevoice_eng.CPRC_abuf_trans_end_set
    __swig_getmethods__["end"] = _cerevoice_eng.CPRC_abuf_trans_end_get
    if _newclass:
        end = _swig_property(_cerevoice_eng.CPRC_abuf_trans_end_get, _cerevoice_eng.CPRC_abuf_trans_end_set)
    __swig_setmethods__["start_sample"] = _cerevoice_eng.CPRC_abuf_trans_start_sample_set
    __swig_getmethods__["start_sample"] = _cerevoice_eng.CPRC_abuf_trans_start_sample_get
    if _newclass:
        start_sample = _swig_property(_cerevoice_eng.CPRC_abuf_trans_start_sample_get, _cerevoice_eng.CPRC_abuf_trans_start_sample_set)
    __swig_setmethods__["end_sample"] = _cerevoice_eng.CPRC_abuf_trans_end_sample_set
    __swig_getmethods__["end_sample"] = _cerevoice_eng.CPRC_abuf_trans_end_sample_get
    if _newclass:
        end_sample = _swig_property(_cerevoice_eng.CPRC_abuf_trans_end_sample_get, _cerevoice_eng.CPRC_abuf_trans_end_sample_set)
    __swig_setmethods__["phone"] = _cerevoice_eng.CPRC_abuf_trans_phone_set
    __swig_getmethods__["phone"] = _cerevoice_eng.CPRC_abuf_trans_phone_get
    if _newclass:
        phone = _swig_property(_cerevoice_eng.CPRC_abuf_trans_phone_get, _cerevoice_eng.CPRC_abuf_trans_phone_set)
    __swig_setmethods__["pidx"] = _cerevoice_eng.CPRC_abuf_trans_pidx_set
    __swig_getmethods__["pidx"] = _cerevoice_eng.CPRC_abuf_trans_pidx_get
    if _newclass:
        pidx = _swig_property(_cerevoice_eng.CPRC_abuf_trans_pidx_get, _cerevoice_eng.CPRC_abuf_trans_pidx_set)
    __swig_setmethods__["stress"] = _cerevoice_eng.CPRC_abuf_trans_stress_set
    __swig_getmethods__["stress"] = _cerevoice_eng.CPRC_abuf_trans_stress_get
    if _newclass:
        stress = _swig_property(_cerevoice_eng.CPRC_abuf_trans_stress_get, _cerevoice_eng.CPRC_abuf_trans_stress_set)
    __swig_setmethods__["sapi_viseme"] = _cerevoice_eng.CPRC_abuf_trans_sapi_viseme_set
    __swig_getmethods__["sapi_viseme"] = _cerevoice_eng.CPRC_abuf_trans_sapi_viseme_get
    if _newclass:
        sapi_viseme = _swig_property(_cerevoice_eng.CPRC_abuf_trans_sapi_viseme_get, _cerevoice_eng.CPRC_abuf_trans_sapi_viseme_set)
    __swig_setmethods__["disney_viseme"] = _cerevoice_eng.CPRC_abuf_trans_disney_viseme_set
    __swig_getmethods__["disney_viseme"] = _cerevoice_eng.CPRC_abuf_trans_disney_viseme_get
    if _newclass:
        disney_viseme = _swig_property(_cerevoice_eng.CPRC_abuf_trans_disney_viseme_get, _cerevoice_eng.CPRC_abuf_trans_disney_viseme_set)
    __swig_setmethods__["sapi_phoneid"] = _cerevoice_eng.CPRC_abuf_trans_sapi_phoneid_set
    __swig_getmethods__["sapi_phoneid"] = _cerevoice_eng.CPRC_abuf_trans_sapi_phoneid_get
    if _newclass:
        sapi_phoneid = _swig_property(_cerevoice_eng.CPRC_abuf_trans_sapi_phoneid_get, _cerevoice_eng.CPRC_abuf_trans_sapi_phoneid_set)
    __swig_setmethods__["mac_phoneid"] = _cerevoice_eng.CPRC_abuf_trans_mac_phoneid_set
    __swig_getmethods__["mac_phoneid"] = _cerevoice_eng.CPRC_abuf_trans_mac_phoneid_get
    if _newclass:
        mac_phoneid = _swig_property(_cerevoice_eng.CPRC_abuf_trans_mac_phoneid_get, _cerevoice_eng.CPRC_abuf_trans_mac_phoneid_set)
    __swig_setmethods__["sylval"] = _cerevoice_eng.CPRC_abuf_trans_sylval_set
    __swig_getmethods__["sylval"] = _cerevoice_eng.CPRC_abuf_trans_sylval_get
    if _newclass:
        sylval = _swig_property(_cerevoice_eng.CPRC_abuf_trans_sylval_get, _cerevoice_eng.CPRC_abuf_trans_sylval_set)

    def __init__(self):
        """__init__(CPRC_abuf_trans self) -> CPRC_abuf_trans"""
        this = _cerevoice_eng.new_CPRC_abuf_trans()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _cerevoice_eng.delete_CPRC_abuf_trans
    __del__ = lambda self: None
CPRC_abuf_trans_swigregister = _cerevoice_eng.CPRC_abuf_trans_swigregister
CPRC_abuf_trans_swigregister(CPRC_abuf_trans)

class CPTP_fixedbuf(_object):
    """Proxy of C++ CPTP_fixedbuf class."""

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CPTP_fixedbuf, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CPTP_fixedbuf, name)
    __repr__ = _swig_repr
    __swig_setmethods__["_size"] = _cerevoice_eng.CPTP_fixedbuf__size_set
    __swig_getmethods__["_size"] = _cerevoice_eng.CPTP_fixedbuf__size_get
    if _newclass:
        _size = _swig_property(_cerevoice_eng.CPTP_fixedbuf__size_get, _cerevoice_eng.CPTP_fixedbuf__size_set)
    __swig_setmethods__["_buffer"] = _cerevoice_eng.CPTP_fixedbuf__buffer_set
    __swig_getmethods__["_buffer"] = _cerevoice_eng.CPTP_fixedbuf__buffer_get
    if _newclass:
        _buffer = _swig_property(_cerevoice_eng.CPTP_fixedbuf__buffer_get, _cerevoice_eng.CPTP_fixedbuf__buffer_set)

    def __init__(self):
        """__init__(CPTP_fixedbuf self) -> CPTP_fixedbuf"""
        this = _cerevoice_eng.new_CPTP_fixedbuf()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _cerevoice_eng.delete_CPTP_fixedbuf
    __del__ = lambda self: None
CPTP_fixedbuf_swigregister = _cerevoice_eng.CPTP_fixedbuf_swigregister
CPTP_fixedbuf_swigregister(CPTP_fixedbuf)


def CPRCEN_engine_new():
    """CPRCEN_engine_new() -> CPRCEN_engine *"""
    return _cerevoice_eng.CPRCEN_engine_new()

def CPRCEN_engine_load_voice(eng, voicef, configf, load_type, licensef, root_certf, certf, cert_key):
    """CPRCEN_engine_load_voice(CPRCEN_engine * eng, char const * voicef, char const * configf, enum CPRC_VOICE_LOAD_TYPE load_type, char const * licensef, char const * root_certf, char const * certf, char const * cert_key) -> int"""
    return _cerevoice_eng.CPRCEN_engine_load_voice(eng, voicef, configf, load_type, licensef, root_certf, certf, cert_key)

def CPRCEN_engine_load_voice_licensestr(eng, license_text, signature, configf, voicef, load_type):
    """CPRCEN_engine_load_voice_licensestr(CPRCEN_engine * eng, char const * license_text, char const * signature, char const * configf, char const * voicef, enum CPRC_VOICE_LOAD_TYPE load_type) -> int"""
    return _cerevoice_eng.CPRCEN_engine_load_voice_licensestr(eng, license_text, signature, configf, voicef, load_type)

def CPRCEN_engine_unload_voice(eng, voice_index):
    """CPRCEN_engine_unload_voice(CPRCEN_engine * eng, int voice_index) -> int"""
    return _cerevoice_eng.CPRCEN_engine_unload_voice(eng, voice_index)

def CPRCEN_engine_load_user_lexicon(eng, voice_index, fname):
    """CPRCEN_engine_load_user_lexicon(CPRCEN_engine * eng, int voice_index, char const * fname) -> int"""
    return _cerevoice_eng.CPRCEN_engine_load_user_lexicon(eng, voice_index, fname)

def CPRCEN_engine_load_user_abbreviations(eng, voice_index, fname):
    """CPRCEN_engine_load_user_abbreviations(CPRCEN_engine * eng, int voice_index, char const * fname) -> int"""
    return _cerevoice_eng.CPRCEN_engine_load_user_abbreviations(eng, voice_index, fname)

def CPRCEN_engine_load_channel_lexicon(eng, chan, fname, lname):
    """CPRCEN_engine_load_channel_lexicon(CPRCEN_engine * eng, CPRCEN_channel_handle chan, char const * fname, char const * lname) -> int"""
    return _cerevoice_eng.CPRCEN_engine_load_channel_lexicon(eng, chan, fname, lname)

def CPRCEN_engine_load_channel_pls(eng, chan, fname, lname):
    """CPRCEN_engine_load_channel_pls(CPRCEN_engine * eng, CPRCEN_channel_handle chan, char const * fname, char const * lname) -> int"""
    return _cerevoice_eng.CPRCEN_engine_load_channel_pls(eng, chan, fname, lname)

def CPRCEN_engine_load_channel_abbreviation(eng, chan, fname, aname):
    """CPRCEN_engine_load_channel_abbreviation(CPRCEN_engine * eng, CPRCEN_channel_handle chan, char const * fname, char const * aname) -> int"""
    return _cerevoice_eng.CPRCEN_engine_load_channel_abbreviation(eng, chan, fname, aname)

def CPRCEN_engine_load_channel_pbreak(eng, chan, fname):
    """CPRCEN_engine_load_channel_pbreak(CPRCEN_engine * eng, CPRCEN_channel_handle chan, char const * fname) -> int"""
    return _cerevoice_eng.CPRCEN_engine_load_channel_pbreak(eng, chan, fname)

def CPRCEN_engine_get_voice_count(eng):
    """CPRCEN_engine_get_voice_count(CPRCEN_engine * eng) -> int"""
    return _cerevoice_eng.CPRCEN_engine_get_voice_count(eng)

def CPRCEN_engine_get_voice_info(eng, voice_index, key):
    """CPRCEN_engine_get_voice_info(CPRCEN_engine * eng, int voice_index, char const * key) -> char const *"""
    return _cerevoice_eng.CPRCEN_engine_get_voice_info(eng, voice_index, key)

def CPRCEN_engine_get_voice_file_info(fname, key):
    """CPRCEN_engine_get_voice_file_info(char const * fname, char const * key) -> char const *"""
    return _cerevoice_eng.CPRCEN_engine_get_voice_file_info(fname, key)

def CPRCEN_engine_open_channel(eng, iso_language_code, iso_region_code, voice_name, srate):
    """CPRCEN_engine_open_channel(CPRCEN_engine * eng, char const * iso_language_code, char const * iso_region_code, char const * voice_name, char const * srate) -> CPRCEN_channel_handle"""
    return _cerevoice_eng.CPRCEN_engine_open_channel(eng, iso_language_code, iso_region_code, voice_name, srate)

def CPRCEN_engine_open_default_channel(eng):
    """CPRCEN_engine_open_default_channel(CPRCEN_engine * eng) -> CPRCEN_channel_handle"""
    return _cerevoice_eng.CPRCEN_engine_open_default_channel(eng)

def CPRCEN_engine_channel_reset(eng, chan):
    """CPRCEN_engine_channel_reset(CPRCEN_engine * eng, CPRCEN_channel_handle chan) -> int"""
    return _cerevoice_eng.CPRCEN_engine_channel_reset(eng, chan)

def CPRCEN_engine_channel_close(eng, chan):
    """CPRCEN_engine_channel_close(CPRCEN_engine * eng, CPRCEN_channel_handle chan) -> int"""
    return _cerevoice_eng.CPRCEN_engine_channel_close(eng, chan)

def CPRCEN_engine_set_callback(eng, chan, userdata, callback):
    """CPRCEN_engine_set_callback(CPRCEN_engine * eng, CPRCEN_channel_handle chan, void * userdata, cprcen_channel_callback callback) -> int"""
    return _cerevoice_eng.CPRCEN_engine_set_callback(eng, chan, userdata, callback)

def CPRCEN_engine_clear_callback(eng, chan):
    """CPRCEN_engine_clear_callback(CPRCEN_engine * eng, CPRCEN_channel_handle chan) -> int"""
    return _cerevoice_eng.CPRCEN_engine_clear_callback(eng, chan)

def CPRCEN_engine_get_channel_userdata(eng, chan):
    """CPRCEN_engine_get_channel_userdata(CPRCEN_engine * eng, CPRCEN_channel_handle chan) -> void *"""
    return _cerevoice_eng.CPRCEN_engine_get_channel_userdata(eng, chan)

def CPRCEN_engine_channel_speak(eng, chan, text, textlen, flush):
    """CPRCEN_engine_channel_speak(CPRCEN_engine * eng, CPRCEN_channel_handle chan, char const * text, int textlen, int flush) -> CPRC_abuf *"""
    return _cerevoice_eng.CPRCEN_engine_channel_speak(eng, chan, text, textlen, flush)

def CPRCEN_engine_channel_interrupt(eng, chan, spurtxml, xmllen, earliest_time, btype, itype):
    """CPRCEN_engine_channel_interrupt(CPRCEN_engine * eng, CPRCEN_channel_handle chan, char const * spurtxml, int xmllen, float earliest_time, enum CPRCEN_INTERRUPT_BOUNDARY_TYPE btype, enum CPRCEN_INTERRUPT_INTERRUPT_TYPE itype) -> CPRC_abuf *"""
    return _cerevoice_eng.CPRCEN_engine_channel_interrupt(eng, chan, spurtxml, xmllen, earliest_time, btype, itype)

def CPRCEN_channel_get_voice_info(eng, chan, key):
    """CPRCEN_channel_get_voice_info(CPRCEN_engine * eng, CPRCEN_channel_handle chan, char const * key) -> char const *"""
    return _cerevoice_eng.CPRCEN_channel_get_voice_info(eng, chan, key)

def CPRCEN_engine_channel_to_file(eng, chan, fname, format):
    """CPRCEN_engine_channel_to_file(CPRCEN_engine * eng, CPRCEN_channel_handle chan, char * fname, enum CPRCEN_AUDIO_FORMAT format) -> int"""
    return _cerevoice_eng.CPRCEN_engine_channel_to_file(eng, chan, fname, format)

def CPRCEN_engine_channel_append_to_file(eng, chan, fname, format):
    """CPRCEN_engine_channel_append_to_file(CPRCEN_engine * eng, CPRCEN_channel_handle chan, char * fname, enum CPRCEN_AUDIO_FORMAT format) -> int"""
    return _cerevoice_eng.CPRCEN_engine_channel_append_to_file(eng, chan, fname, format)

def CPRCEN_engine_channel_force_append_to_file(eng, chan, fname, format):
    """CPRCEN_engine_channel_force_append_to_file(CPRCEN_engine * eng, CPRCEN_channel_handle chan, char * fname, enum CPRCEN_AUDIO_FORMAT format) -> int"""
    return _cerevoice_eng.CPRCEN_engine_channel_force_append_to_file(eng, chan, fname, format)

def CPRCEN_engine_channel_no_file(eng, chan):
    """CPRCEN_engine_channel_no_file(CPRCEN_engine * eng, CPRCEN_channel_handle chan) -> int"""
    return _cerevoice_eng.CPRCEN_engine_channel_no_file(eng, chan)

def CPRCEN_channel_synth_type_usel(eng, chan):
    """CPRCEN_channel_synth_type_usel(CPRCEN_engine * eng, CPRCEN_channel_handle chan) -> int"""
    return _cerevoice_eng.CPRCEN_channel_synth_type_usel(eng, chan)

def CPRCEN_channel_set_phone_min_max(eng, chan, min, max):
    """CPRCEN_channel_set_phone_min_max(CPRCEN_engine * eng, CPRCEN_channel_handle chan, int min, int max) -> int"""
    return _cerevoice_eng.CPRCEN_channel_set_phone_min_max(eng, chan, min, max)

def CPRCEN_channel_set_pipe_length(eng, chan, pipelen):
    """CPRCEN_channel_set_pipe_length(CPRCEN_engine * eng, CPRCEN_channel_handle chan, int pipelen) -> int"""
    return _cerevoice_eng.CPRCEN_channel_set_pipe_length(eng, chan, pipelen)

def CPRC_abuf_get_trans(ab, i):
    """CPRC_abuf_get_trans(CPRC_abuf * ab, int i) -> CPRC_abuf_trans const *"""
    return _cerevoice_eng.CPRC_abuf_get_trans(ab, i)

def CPRC_abuf_trans_sz(ab):
    """CPRC_abuf_trans_sz(CPRC_abuf * ab) -> int"""
    return _cerevoice_eng.CPRC_abuf_trans_sz(ab)

def CPRC_abuf_trans_name(t):
    """CPRC_abuf_trans_name(CPRC_abuf_trans const * t) -> char const *"""
    return _cerevoice_eng.CPRC_abuf_trans_name(t)

def CPRC_abuf_trans_type(t):
    """CPRC_abuf_trans_type(CPRC_abuf_trans const * t) -> enum CPRC_ABUF_TRANS"""
    return _cerevoice_eng.CPRC_abuf_trans_type(t)

def CPRC_abuf_trans_start(t):
    """CPRC_abuf_trans_start(CPRC_abuf_trans const * t) -> float"""
    return _cerevoice_eng.CPRC_abuf_trans_start(t)

def CPRC_abuf_trans_end(t):
    """CPRC_abuf_trans_end(CPRC_abuf_trans const * t) -> float"""
    return _cerevoice_eng.CPRC_abuf_trans_end(t)

def CPRC_abuf_trans_start_sample(t):
    """CPRC_abuf_trans_start_sample(CPRC_abuf_trans const * t) -> int"""
    return _cerevoice_eng.CPRC_abuf_trans_start_sample(t)

def CPRC_abuf_trans_end_sample(t):
    """CPRC_abuf_trans_end_sample(CPRC_abuf_trans const * t) -> int"""
    return _cerevoice_eng.CPRC_abuf_trans_end_sample(t)

def CPRC_abuf_trans_phone_stress(t):
    """CPRC_abuf_trans_phone_stress(CPRC_abuf_trans const * t) -> int"""
    return _cerevoice_eng.CPRC_abuf_trans_phone_stress(t)

def CPRC_abuf_trans_sapi_viseme(t):
    """CPRC_abuf_trans_sapi_viseme(CPRC_abuf_trans const * t) -> int"""
    return _cerevoice_eng.CPRC_abuf_trans_sapi_viseme(t)

def CPRC_abuf_trans_disney_viseme(t):
    """CPRC_abuf_trans_disney_viseme(CPRC_abuf_trans const * t) -> int"""
    return _cerevoice_eng.CPRC_abuf_trans_disney_viseme(t)

def CPRC_abuf_trans_sapi_phoneid(t):
    """CPRC_abuf_trans_sapi_phoneid(CPRC_abuf_trans const * t) -> int"""
    return _cerevoice_eng.CPRC_abuf_trans_sapi_phoneid(t)

def CPRC_abuf_trans_mac_phoneid(t):
    """CPRC_abuf_trans_mac_phoneid(CPRC_abuf_trans const * t) -> int"""
    return _cerevoice_eng.CPRC_abuf_trans_mac_phoneid(t)

def CPRC_abuf_wav_sz(ab):
    """CPRC_abuf_wav_sz(CPRC_abuf * ab) -> int"""
    return _cerevoice_eng.CPRC_abuf_wav_sz(ab)

def CPRC_abuf_wav(ab, i):
    """CPRC_abuf_wav(CPRC_abuf * ab, int i) -> short"""
    return _cerevoice_eng.CPRC_abuf_wav(ab, i)

def CPRC_abuf_wav_data(ab):
    """CPRC_abuf_wav_data(CPRC_abuf * ab) -> short *"""
    return _cerevoice_eng.CPRC_abuf_wav_data(ab)

def CPRC_abuf_wav_mk(ab):
    """CPRC_abuf_wav_mk(CPRC_abuf * ab) -> int"""
    return _cerevoice_eng.CPRC_abuf_wav_mk(ab)

def CPRC_abuf_wav_done(ab):
    """CPRC_abuf_wav_done(CPRC_abuf * ab) -> int"""
    return _cerevoice_eng.CPRC_abuf_wav_done(ab)

def CPRC_abuf_added_wav_sz(ab):
    """CPRC_abuf_added_wav_sz(CPRC_abuf * ab) -> int"""
    return _cerevoice_eng.CPRC_abuf_added_wav_sz(ab)

def CPRC_abuf_trans_mk(ab):
    """CPRC_abuf_trans_mk(CPRC_abuf * ab) -> int"""
    return _cerevoice_eng.CPRC_abuf_trans_mk(ab)

def CPRC_abuf_trans_done(ab):
    """CPRC_abuf_trans_done(CPRC_abuf * ab) -> int"""
    return _cerevoice_eng.CPRC_abuf_trans_done(ab)

def CPRC_abuf_wav_srate(ab):
    """CPRC_abuf_wav_srate(CPRC_abuf * ab) -> int"""
    return _cerevoice_eng.CPRC_abuf_wav_srate(ab)

def CPRC_riff_save(wav, fname):
    """CPRC_riff_save(CPRC_abuf * wav, char const * fname) -> int"""
    return _cerevoice_eng.CPRC_riff_save(wav, fname)

def CPRC_riff_append(wav, fname):
    """CPRC_riff_append(CPRC_abuf * wav, char const * fname) -> int"""
    return _cerevoice_eng.CPRC_riff_append(wav, fname)

def CPRC_riff_save_trans(wav, fname):
    """CPRC_riff_save_trans(CPRC_abuf * wav, char const * fname) -> int"""
    return _cerevoice_eng.CPRC_riff_save_trans(wav, fname)

def CPRC_riff_buffer(wav):
    """CPRC_riff_buffer(CPRC_abuf * wav) -> CPTP_fixedbuf *"""
    return _cerevoice_eng.CPRC_riff_buffer(wav)

def CPTP_fixedbuf_delete(fb):
    """CPTP_fixedbuf_delete(CPTP_fixedbuf * fb)"""
    return _cerevoice_eng.CPTP_fixedbuf_delete(fb)

def CPRC_abuf_copy(ab):
    """CPRC_abuf_copy(CPRC_abuf * ab) -> CPRC_abuf *"""
    return _cerevoice_eng.CPRC_abuf_copy(ab)

def CPRC_abuf_extract(ab, offset, sz):
    """CPRC_abuf_extract(CPRC_abuf * ab, int offset, int sz) -> CPRC_abuf *"""
    return _cerevoice_eng.CPRC_abuf_extract(ab, offset, sz)

def CPRC_abuf_delete(ab):
    """CPRC_abuf_delete(CPRC_abuf * ab)"""
    return _cerevoice_eng.CPRC_abuf_delete(ab)

def CPRC_abuf_append(ab_out, ab_in):
    """CPRC_abuf_append(CPRC_abuf * ab_out, CPRC_abuf * ab_in) -> CPRC_abuf *"""
    return _cerevoice_eng.CPRC_abuf_append(ab_out, ab_in)

def CPRCEN_major_version():
    """CPRCEN_major_version() -> int"""
    return _cerevoice_eng.CPRCEN_major_version()

def CPRCEN_minor_version():
    """CPRCEN_minor_version() -> int"""
    return _cerevoice_eng.CPRCEN_minor_version()

def CPRCEN_revision_number():
    """CPRCEN_revision_number() -> int"""
    return _cerevoice_eng.CPRCEN_revision_number()
CPRCEN_CHAN_FULL = _cerevoice_eng.CPRCEN_CHAN_FULL
CPRCEN_CHAN_TK = _cerevoice_eng.CPRCEN_CHAN_TK
CPRCEN_CHAN_BACK = _cerevoice_eng.CPRCEN_CHAN_BACK
CPRCEN_CHAN_NORM = _cerevoice_eng.CPRCEN_CHAN_NORM
CPRCEN_CHAN_SPURT = _cerevoice_eng.CPRCEN_CHAN_SPURT
CPRCEN_CHAN_ABOOK = _cerevoice_eng.CPRCEN_CHAN_ABOOK
CPRCEN_SYNTH_NONE = _cerevoice_eng.CPRCEN_SYNTH_NONE
CPRCEN_SYNTH_USEL = _cerevoice_eng.CPRCEN_SYNTH_USEL
CPRCEN_SYNTH_DNNPROS = _cerevoice_eng.CPRCEN_SYNTH_DNNPROS
CPRCEN_SYNTH_DNN = _cerevoice_eng.CPRCEN_SYNTH_DNN
CPRCEN_PROSODY_RAW = _cerevoice_eng.CPRCEN_PROSODY_RAW
CPRCEN_PROSODY_DNN = _cerevoice_eng.CPRCEN_PROSODY_DNN
CPDNN_FEATURE_IDX_NONE = _cerevoice_eng.CPDNN_FEATURE_IDX_NONE
CPDNN_FEATURE_IDX_START = _cerevoice_eng.CPDNN_FEATURE_IDX_START
CPDNN_FEATURE_IDX_INPUT = _cerevoice_eng.CPDNN_FEATURE_IDX_INPUT
CPDNN_FEATURE_IDX_PROS_TGT_START = _cerevoice_eng.CPDNN_FEATURE_IDX_PROS_TGT_START
CPDNN_FEATURE_IDX_F0_TGT = _cerevoice_eng.CPDNN_FEATURE_IDX_F0_TGT
CPDNN_FEATURE_IDX_DUR_TGT = _cerevoice_eng.CPDNN_FEATURE_IDX_DUR_TGT
CPDNN_FEATURE_IDX_NRG_TGT = _cerevoice_eng.CPDNN_FEATURE_IDX_NRG_TGT
CPDNN_FEATURE_IDX_PROS_TGT_END = _cerevoice_eng.CPDNN_FEATURE_IDX_PROS_TGT_END
CPDNN_FEATURE_IDX_ACF_POS_PRE = _cerevoice_eng.CPDNN_FEATURE_IDX_ACF_POS_PRE
CPDNN_FEATURE_IDX_ACF_POS_PST = _cerevoice_eng.CPDNN_FEATURE_IDX_ACF_POS_PST
CPDNN_FEATURE_IDX_SPEECH_FEATURES_START = _cerevoice_eng.CPDNN_FEATURE_IDX_SPEECH_FEATURES_START
CPDNN_FEATURE_IDX_ACF_MCEP = _cerevoice_eng.CPDNN_FEATURE_IDX_ACF_MCEP
CPDNN_FEATURE_IDX_ACF_CEP = _cerevoice_eng.CPDNN_FEATURE_IDX_ACF_CEP
CPDNN_FEATURE_IDX_ACF_LSF = _cerevoice_eng.CPDNN_FEATURE_IDX_ACF_LSF
CPDNN_FEATURE_IDX_ACF_BLSF = _cerevoice_eng.CPDNN_FEATURE_IDX_ACF_BLSF
CPDNN_FEATURE_IDX_ACF_PVOICE = _cerevoice_eng.CPDNN_FEATURE_IDX_ACF_PVOICE
CPDNN_FEATURE_IDX_ACF_LF0 = _cerevoice_eng.CPDNN_FEATURE_IDX_ACF_LF0
CPDNN_FEATURE_IDX_ACF_BNDAP = _cerevoice_eng.CPDNN_FEATURE_IDX_ACF_BNDAP
CPDNN_FEATURE_IDX_ACF_PLS_COEF = _cerevoice_eng.CPDNN_FEATURE_IDX_ACF_PLS_COEF
CPDNN_FEATURE_IDX_ACF_ENERGY = _cerevoice_eng.CPDNN_FEATURE_IDX_ACF_ENERGY
CPDNN_FEATURE_IDX_ACF_MISC = _cerevoice_eng.CPDNN_FEATURE_IDX_ACF_MISC
CPDNN_FEATURE_IDX_SPEECH_FEATURES_END = _cerevoice_eng.CPDNN_FEATURE_IDX_SPEECH_FEATURES_END
CPDNN_FEATURE_IDX_LEN = _cerevoice_eng.CPDNN_FEATURE_IDX_LEN

def CPRCEN_engine_open_channel_with_type(eng, type, iso_language_code, iso_region_code, voice_code, srate):
    """CPRCEN_engine_open_channel_with_type(CPRCEN_engine * eng, enum CPRCEN_CHANNEL_TYPE type, char const * iso_language_code, char const * iso_region_code, char const * voice_code, char const * srate) -> CPRCEN_channel_handle"""
    return _cerevoice_eng.CPRCEN_engine_open_channel_with_type(eng, type, iso_language_code, iso_region_code, voice_code, srate)

def CPRCEN_channel_get_cerevoice(eng, hc):
    """CPRCEN_channel_get_cerevoice(CPRCEN_engine * eng, CPRCEN_channel_handle hc) -> CPRC_voice *"""
    return _cerevoice_eng.CPRCEN_channel_get_cerevoice(eng, hc)

def CPRCEN_channel_get_cerevoice_hybrid(eng, hc):
    """CPRCEN_channel_get_cerevoice_hybrid(CPRCEN_engine * eng, CPRCEN_channel_handle hc) -> CPRC_voice *"""
    return _cerevoice_eng.CPRCEN_channel_get_cerevoice_hybrid(eng, hc)

def CPRCEN_engine_chan_text_process(eng, chan, text, textlen, flush):
    """CPRCEN_engine_chan_text_process(CPRCEN_engine * eng, CPRCEN_channel_handle chan, char const * text, int textlen, int flush) -> char const *"""
    return _cerevoice_eng.CPRCEN_engine_chan_text_process(eng, chan, text, textlen, flush)

def CPRCEN_engine_channel_speak_spurt(eng, chan, text, textlen):
    """CPRCEN_engine_channel_speak_spurt(CPRCEN_engine * eng, CPRCEN_channel_handle chan, char const * text, int textlen) -> CPRC_abuf *"""
    return _cerevoice_eng.CPRCEN_engine_channel_speak_spurt(eng, chan, text, textlen)

def CPRCEN_engine_channel_interrupt_legacy(eng, chan, text, textlen, earliest_time, btype, itype, flush):
    """CPRCEN_engine_channel_interrupt_legacy(CPRCEN_engine * eng, CPRCEN_channel_handle chan, char const * text, int textlen, float earliest_time, enum CPRCEN_INTERRUPT_BOUNDARY_TYPE btype, enum CPRCEN_INTERRUPT_INTERRUPT_TYPE itype, int flush) -> CPRC_abuf *"""
    return _cerevoice_eng.CPRCEN_engine_channel_interrupt_legacy(eng, chan, text, textlen, earliest_time, btype, itype, flush)

def CPRCEN_engine_chan_get_last_spurt(eng, chan):
    """CPRCEN_engine_chan_get_last_spurt(CPRCEN_engine * eng, CPRCEN_channel_handle chan) -> char const *"""
    return _cerevoice_eng.CPRCEN_engine_chan_get_last_spurt(eng, chan)

def CPRCEN_engine_chan_get_last_tpspurt(eng, chan):
    """CPRCEN_engine_chan_get_last_tpspurt(CPRCEN_engine * eng, CPRCEN_channel_handle chan) -> char const *"""
    return _cerevoice_eng.CPRCEN_engine_chan_get_last_tpspurt(eng, chan)

def CPRCEN_engine_chan_get_last_spurt_struct(eng, chan):
    """CPRCEN_engine_chan_get_last_spurt_struct(CPRCEN_engine * eng, CPRCEN_channel_handle chan) -> CPRC_spurt *"""
    return _cerevoice_eng.CPRCEN_engine_chan_get_last_spurt_struct(eng, chan)

def CPRCEN_engine_chan_get_last_units(eng, chan):
    """CPRCEN_engine_chan_get_last_units(CPRCEN_engine * eng, CPRCEN_channel_handle chan) -> char const *"""
    return _cerevoice_eng.CPRCEN_engine_chan_get_last_units(eng, chan)

def CPRCEN_engine_set_text_callback(eng, chan, userdata, text_callback):
    """CPRCEN_engine_set_text_callback(CPRCEN_engine * eng, CPRCEN_channel_handle chan, void * userdata, cprcen_channel_text_callback text_callback) -> int"""
    return _cerevoice_eng.CPRCEN_engine_set_text_callback(eng, chan, userdata, text_callback)

def CPRCEN_engine_clear_application_callback(eng, chan):
    """CPRCEN_engine_clear_application_callback(CPRCEN_engine * eng, CPRCEN_channel_handle chan) -> int"""
    return _cerevoice_eng.CPRCEN_engine_clear_application_callback(eng, chan)

def CPRCEN_engine_set_application_callback(eng, chan, userdata, text_callback):
    """CPRCEN_engine_set_application_callback(CPRCEN_engine * eng, CPRCEN_channel_handle chan, void * userdata, cprcen_channel_text_callback text_callback) -> int"""
    return _cerevoice_eng.CPRCEN_engine_set_application_callback(eng, chan, userdata, text_callback)

def CPRCEN_engine_get_channel_application_userdata(eng, chan):
    """CPRCEN_engine_get_channel_application_userdata(CPRCEN_engine * eng, CPRCEN_channel_handle chan) -> void *"""
    return _cerevoice_eng.CPRCEN_engine_get_channel_application_userdata(eng, chan)

def CPRCEN_engine_clear_text_callback(eng, chan):
    """CPRCEN_engine_clear_text_callback(CPRCEN_engine * eng, CPRCEN_channel_handle chan) -> int"""
    return _cerevoice_eng.CPRCEN_engine_clear_text_callback(eng, chan)

def CPRCEN_channel_get(eng, chan):
    """CPRCEN_channel_get(CPRCEN_engine * eng, CPRCEN_channel_handle chan) -> CPRCEN_channel *"""
    return _cerevoice_eng.CPRCEN_channel_get(eng, chan)

def CPRCEN_channel_fx(c, spurtxml):
    """CPRCEN_channel_fx(CPRCEN_channel * c, char const * spurtxml)"""
    return _cerevoice_eng.CPRCEN_channel_fx(c, spurtxml)

def CPRCEN_channel_audio_from_file(eng, chan, filename):
    """CPRCEN_channel_audio_from_file(CPRCEN_engine * eng, CPRCEN_channel_handle chan, char const * filename) -> int"""
    return _cerevoice_eng.CPRCEN_channel_audio_from_file(eng, chan, filename)

def CPRCEN_channel_synth_get_type(eng, chan):
    """CPRCEN_channel_synth_get_type(CPRCEN_engine * eng, CPRCEN_channel_handle chan) -> enum CPRCEN_SYNTH_TYPE"""
    return _cerevoice_eng.CPRCEN_channel_synth_get_type(eng, chan)

def CPRCEN_voice_synthtype(v):
    """CPRCEN_voice_synthtype(CPRCEN_voice * v) -> enum CPRCEN_SYNTH_TYPE"""
    return _cerevoice_eng.CPRCEN_voice_synthtype(v)

def CPRCEN_get_synthtype_name(stype):
    """CPRCEN_get_synthtype_name(enum CPRCEN_SYNTH_TYPE stype) -> char const *"""
    return _cerevoice_eng.CPRCEN_get_synthtype_name(stype)

def CPRCEN_channel_set_abuf_append(c, val):
    """CPRCEN_channel_set_abuf_append(CPRCEN_channel * c, int val)"""
    return _cerevoice_eng.CPRCEN_channel_set_abuf_append(c, val)

def CPRCEN_engine_channel_logger(eng, chan):
    """CPRCEN_engine_channel_logger(CPRCEN_engine * eng, CPRCEN_channel_handle chan) -> CPTP_logger *"""
    return _cerevoice_eng.CPRCEN_engine_channel_logger(eng, chan)

def CPRCEN_engine_channel_set_normaliser_tracing(eng, chan, tracing):
    """CPRCEN_engine_channel_set_normaliser_tracing(CPRCEN_engine * eng, CPRCEN_channel_handle chan, int tracing)"""
    return _cerevoice_eng.CPRCEN_engine_channel_set_normaliser_tracing(eng, chan, tracing)

def CPRC_abuf_set_wav(ab, pywav, pylen):
    """CPRC_abuf_set_wav(CPRC_abuf * ab, wavedata * pywav, int pylen)"""
    return _cerevoice_eng.CPRC_abuf_set_wav(ab, pywav, pylen)

def CPRC_append_phoneme_trans(wav, fname):
    """CPRC_append_phoneme_trans(CPRC_abuf * wav, char const * fname) -> int"""
    return _cerevoice_eng.CPRC_append_phoneme_trans(wav, fname)

def CPRCEN_engine_channel_dnnspt(eng, chan):
    """CPRCEN_engine_channel_dnnspt(CPRCEN_engine * eng, CPRCEN_channel_handle chan) -> CPDNN_dnnspurt *"""
    return _cerevoice_eng.CPRCEN_engine_channel_dnnspt(eng, chan)

def CPDNN_dnnspurt_set_dump_dir(dnnspt, dirname):
    """CPDNN_dnnspurt_set_dump_dir(CPDNN_dnnspurt * dnnspt, char const * dirname) -> int"""
    return _cerevoice_eng.CPDNN_dnnspurt_set_dump_dir(dnnspt, dirname)

def CPDNN_dnnspurt_fshift(dnnspt):
    """CPDNN_dnnspurt_fshift(CPDNN_dnnspurt * dnnspt) -> float"""
    return _cerevoice_eng.CPDNN_dnnspurt_fshift(dnnspt)

def CPDNN_dnnspurt_generated_parameters(dnnspt, sftidx):
    """CPDNN_dnnspurt_generated_parameters(CPDNN_dnnspurt * dnnspt, enum CPDNN_FEATURE_IDX sftidx) -> CPTP_doublematrix *"""
    return _cerevoice_eng.CPDNN_dnnspurt_generated_parameters(dnnspt, sftidx)

def CPDNN_feature_name(sftidx):
    """CPDNN_feature_name(enum CPDNN_FEATURE_IDX sftidx) -> char const *"""
    return _cerevoice_eng.CPDNN_feature_name(sftidx)

def CPRCEN_engine_load_voice_dir(eng, voicef, configf, load_type, licensef, certdir):
    """CPRCEN_engine_load_voice_dir(CPRCEN_engine * eng, char const * voicef, char const * configf, enum CPRC_VOICE_LOAD_TYPE load_type, char const * licensef, char const * certdir) -> int"""
    return _cerevoice_eng.CPRCEN_engine_load_voice_dir(eng, voicef, configf, load_type, licensef, certdir)

__version__ = "{0}.{1}.{2}".format(CPRCEN_major_version(), CPRCEN_minor_version(), CPRCEN_revision_number())

# This file is compatible with both classic and new-style classes.

