#!/usr/bin/env python
# -*- coding: utf-8 -*-

import speech_recognition as sr


class VoiceControl():

    def listen_commands(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)

        '''
        # recognize speech using Sphinx
        try:
            print("Sphinx thinks you said " + r.recognize_sphinx(audio))
        except sr.UnknownValueError:
            print("Sphinx could not understand audio")
        except sr.RequestError as e:
            print("Sphinx error; {0}".format(e))
        '''

        try:
            words = r.recognize_google(audio, None, 'pl-PL')
            print("Google Speech Recognition thinks you said " + words)
            if words == 'dupa':
                print 'chyba ty!'
            self.listen_commands()
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            self.listen_commands()
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

if __name__ == '__main__':
    VoiceControl().listen_commands()
