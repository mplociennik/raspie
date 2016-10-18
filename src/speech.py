#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2
import pyvona
from audio import Audio


IVONA_ACCESS_KEY = 'GDNAIKZKKGPM3SPFPZGA'
IVONA_SECRET_KEY = 'PXnXmq3aV1qYsV4jxG4WtoVhESq4gZaXGjrDTBke'

class Speech(object):
    """Class to making connection to voice webapi."""
    
    def hello(self, text):
        self.create_speech(text)

    def filter_spaces(self, text):
        return text.replace(" ", "%20")

    def create_voice(self, text):
        """"""
        v = pyvona.create_voice(IVONA_ACCESS_KEY, IVONA_SECRET_KEY)
        v.voice_name = 'Jacek'

        try:
            v.speak(text)
        except:
            print "Speech: connection not found!"

    def play_sound(self, file):
        Audio(file, 1.0)

if __name__ == "__main__":
    speech = Speech()
    speech.hello('Hello World!')
