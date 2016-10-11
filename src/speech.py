#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2
import mp3play
import pyvona

IVONA_ACCESS_KEY = 'GDNAIKZKKGPM3SPFPZGA'
IVONA_SECRET_KEY = 'PXnXmq3aV1qYsV4jxG4WtoVhESq4gZaXGjrDTBke'

class Speech(object):
    """Class to making connection to voice webapi."""
    
    def hello(self, text):
        self.create_speech(text)

    def filter_spaces(self, text):
        return text.replace(" ", "%20")

    def create_voice_web(self, text):
        """"""
        url_speak = "http://127.0.0.1:8000/speech?text=" + self.filter_spaces(text)
        try:
            response = urllib2.urlopen(url_speak)
            print response
        except:
            print "Speech: connection not found!"    

    def create_voice(self, text):
        """"""
        v = pyvona.create_voice(IVONA_ACCESS_KEY, 
                                    IVONA_SECRET_KEY)
        v.voice_name = 'Eric'

        try:
            v.speak(text)
        except:
            print "Speech: connection not found!"

    def play_sound(self, file):
        sound = mp3play.load(file)
        sound.play()
        time.sleep(min(30, sound.seconds()))
        sound.stop()

if __name__ == "__main__":
    speech = Speech()
    speech.hello('Hello World!')
