#!/usr/bin/env python
# -*- coding: utf-8 -*-

import speech_recognition as sr
from multiprocessing import Process, Queue
from pymove import PyMove
from speech import Speech


class VoiceControl():
'''want to install pyaudio https://www.raspberrypi.org/forums/viewtopic.php?t=25173 '''
    def robot_autopilot(self):
        text = 'Starting autopilot'
        speech = Speech()
        speech.create_voice(text)
        autopilot = PyMove()
        q_state = Queue()
        autopilot_process = Process(target=autopilot.autopilot_process, args=(q_state,))
        autopilot_process.start()

    def listen_commands(self):
        r = sr.Recognizer()
        m = sr.Microphone(2, sample_rate = 48000, device_index = 2, chunk_size = 1024)

        with m as source: r.adjust_for_ambient_noise(source)
        print("Set minimum energy threshold to {}".format(r.energy_threshold))
        print("Say something!")
        with m as source: audio = r.listen(source)
        print("Got it! Now to recognize it {0}").format(r.recognize_sphinx(audio))
#        with sr.Microphone(device_index=2) as source:
#            print("Say something!")
#            audio = r.listen(source)

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
            words = r.recognize_google(audio, None, 'en-US')
#            words = r.recognize_sphinx(audio)
            print("PocketSphinx Speech Recognition thinks you said: " + words)
            if 'Raspie' in words:
                text = 'Listening you.'
                speech = Speech()
                speech.create_voice(text)
                print text
            if 'autopilot' in words:
                text = 'Starting autopilot'
                speech = Speech()
                speech.create_voice(text)
                self.robot_autopilot()
            if 'about' in words:
                text = 'I\'m Raspie Robot version 1.0, home assistant created by Cieniu.'
                speech = Speech()
                speech.create_voice(text)
            self.listen_commands()
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            self.listen_commands()
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service: {0}".format(e))

if __name__ == '__main__':
    VoiceControl().listen_commands()
