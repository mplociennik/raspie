#!/usr/bin/env python
# -*- coding: utf-8 -*-
import multiprocessing
import os
import time
from pymove import PyMove
from speech import Speech

def webapi():
    os.system('venv/bin/python webapi/manage.py runserver 0.0.0.0:8000')

def move_control():
    move_control = PyMove()
    move_control.start()
    return move_control

def voice_commands():
    print "voice_commands"

def cam_recording():
    print "cam_recording"

def welcome():
    print "started..."
    speech = Speech()
    speech.play_sound('sounds/Processing_R2D2.mp3')

if __name__ == '__main__':
    jobs = []
#    webapi = multiprocessing.Process(target=webapi)
    move_control = multiprocessing.Process(target=move_control)
    voice_commands = multiprocessing.Process(target=voice_commands)
    cam_recording = multiprocessing.Process(target=cam_recording)
    welcome = multiprocessing.Process(target=welcome)
#    jobs.append(webapi)
    jobs.append(move_control)
    jobs.append(voice_commands)
    jobs.append(cam_recording)
    jobs.append(welcome)
#    webapi.start()
    move_control.start()
    voice_commands.start()
    cam_recording.start()
    welcome.start()