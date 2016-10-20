#!/usr/bin/env python
# -*- coding: utf-8 -*-

import speech_recognition as sr
from multiprocessing import Process, Queue
#from pymove import PyMove
from speech import Speech


class VoiceControl():

    def robot_autopilot(self):
        text = 'Starting autopilot'
        speech = Speech()
        speech.create_voice(text)
        #autopilot = PyMove()
        #q_state = Queue()
        #autopilot_process = Process(target=autopilot.autopilot_process, args=(q_state,))
        #autopilot_process.start()

    def listen_commands(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Waiting for command")
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
            print("Google Speech Recognition thinks you said: " + words)
            speech = Speech()
            speech.create_voice(words)
            if words == 'Raspie':
                text = 'Listening you.'
                speech = Speech()
                speech.create_voice(text)
                print text
            if words == 'dupa':
                text = 'Nie mów brzydko.'
                speech = Speech()
                speech.create_voice(text)
                print text
            if words == 'autopilot':
                text = 'Starting autopilot'
                speech = Speech()
                speech.create_voice(text)
                self.robot_autopilot()
            self.listen_commands()
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            self.listen_commands()
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

if __name__ == '__main__':
    VoiceControl().listen_commands()