#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time
from key_control import KeyControlProcess
from audio import Audio
from voice_control import VoiceControl

def webapi():
    os.system('venv/bin/python webapi/manage.py runserver 0.0.0.0:8000')

def key_control():
    key_control = KeyControl()
    key_control.start()

def voice_commands():
    voice_control_process = VoiceControl()
    voice_control_process.start()

def cam_recording():
    print "cam_recording"

def welcome():
    print "started..."
    Audio('sounds/Processing_R2D2.mp3', 1.0)

if __name__ == '__main__':
    self.welcome()
    self.key_control()
    self.voice_commands()