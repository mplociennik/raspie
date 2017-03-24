#!/usr/bin/env python
# -*- coding: utf-8 -*-

from speech_recognizer import SpeechRecognizer
from multiprocessing import Process, Queue
from pymove import PyMove
from speech import Speech
from autopilot import RaspieAutopilotProcess
from weatcher import Weatcher


class VoiceControl(Process):
    
    def __init__(self, ):
        multiprocessing.Process.__init__(self)
        self.exit = multiprocessing.Event()
    
    def command_weatcher(self):
        weather = Weather().check_weather()
        text = weather['forecast']['txt_forecast']['forecastday'][0]['fcttext_metric']
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

    def command_dance(self):
        text = 'Exterminate, exterminate, exterminate!'
        speech = Speech()
        speech.create_voice(text)
        return True
    
    def listen_commands(self):
        text = "How I can help You."
        speech = Speech()
        speech.create_voice(text)
        r = SpeechRecognizer()
        command = (r.recognize()).lower()
        print 'Recognized command: {0}'.format(command)
        if 'weatcher' in command:
            self.command_weatcher()
        if 'autopilot' in command:
            self.command_autopilot()
        if 'dance' in command:
            self.command_dance()
        if 'exterminate' in command:
            self.command_exterminate()
            
    def listen_text(self):
        r = SpeechRecognizer()
        text = (r.recognize()).lower()
        print 'Recognized text: {0}'.format(text)
        if 'shadow' in text:
            self.listen_commands()
            
    def start(self):
        while not self.exit.is_set():
            self.listen_text()
        print "Voice listening stoped!"

    def terminate(self):
        print "Terminating autopilot..."
        self.exit.set() 
            
if __name__ == '__main__':
    VoiceControl().start()
