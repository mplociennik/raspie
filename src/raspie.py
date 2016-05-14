import multiprocessing
import os
import time
import urllib2
import pymove

def filter_spaces(text):
    return text.replace(" ", "%20")

def create_speech(text):
    url_speak = "http://127.0.0.1:8000/speech?text=" + filter_spaces(text)
    response = urllib2.urlopen(url_speak)
    print response

def webapi():
    os.system('venv/bin/python webapi/manage.py runserver 0.0.0.0:8000')

def move_control():
    move_control = PyMove()
    move_control.start()
    return move_control

def distance_detection():
    print "distance_detection"

def voice_recording():
    print "voice_recording"

def cam_recording():
    print "cam_recording"

def welcome():
    text = "Witaj panie"
    create_speech(text)

if __name__ == '__main__':
    jobs = []
    webapi = multiprocessing.Process(target=webapi)
    move_control = multiprocessing.Process(target=move_control)
    distance_detection = multiprocessing.Process(target=distance_detection)
    voice_recording = multiprocessing.Process(target=voice_recording)
    cam_recording = multiprocessing.Process(target=cam_recording)
    welcome = multiprocessing.Process(target=welcome)
    jobs.append(webapi)
    jobs.append(move_control)
    jobs.append(distance_detection)
    jobs.append(voice_recording)
    jobs.append(cam_recording)
    jobs.append(welcome)
    webapi.start()
    time.sleep(10)
    move_control.start()
    distance_detection.start()
    voice_recording.start()
    cam_recording.start()
    welcome.start()