#!/usr/bin/env python
# -*- coding: utf-8 -*-

from speech_recognizer import SpeechRecognizer
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
    
    def command_weatcher(self):
        print "Weatcher!"
        return True
    
    def command_autopilot(self):
        print 'Autopilot!'
        return True
    
    def command_dance(self):
        print 'Lets Dance!'
        return True
    
    def listen_commands(self):
        r = SpeechRecognizer()
        command = (r.recognize()).lower()
        if 'weatcher' in command:
            self.command_weatcher()
        if 'autopilot' in command:
            self.command_autopilot()
        if 'dance' in command:
            self.command_dance()
            
    def listen_text(self):
        r = SpeechRecognizer()
        text = r.recognize()
        if text == 'shadow':
            self.listen_commands()
            
            
if __name__ == '__main__':
    VoiceControl().listen_text()
