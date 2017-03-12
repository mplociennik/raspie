#!/usr/bin/env python
# -*- coding: utf-8 -*-

from speech_recognizer import SpeechRecognizer
from multiprocessing import Process, Queue
from pymove import PyMove
from speech import Speech
from autopilot import RaspieAutopilotProcess


class VoiceControl():
    
    def command_weatcher(self):
        text = "Weatcher!"
        speech = Speech()
        speech.create_voice(text)
        return True
    
    def command_autopilot(self):
        text = 'Runing autopilot!'
        speech = Speech()
        speech.create_voice(text)
        process = RaspieAutopilotProcess()
        process.start()
        return True
    
    def command_dance(self):
        text = 'Lets Dance!'
        speech = Speech()
        speech.create_voice(text)
        return True
    
    def listen_commands(self):
        text = "I am listening your commands."
        speech = Speech()
        speech.create_voice(text)
        r = SpeechRecognizer()
        command = (r.recognize()).lower()
        print 'Recognized command: {}'.format(command)
        if 'weatcher' in command:
            self.command_weatcher()
        if 'autopilot' in command:
            self.command_autopilot()
        if 'dance' in command:
            self.command_dance()
            
    def listen_text(self):
        r = SpeechRecognizer()
        text = (r.recognize()).lower()
        print 'Recognized text: {0}'.format(text)
        if 'shadow' in text:
            self.listen_commands()
            
            
if __name__ == '__main__':
    VoiceControl().listen_text()
