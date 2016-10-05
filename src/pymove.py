#!/usr/bin/env python
# -*- coding: utf-8 -*-
import RPi.GPIO as gpio
from distance import Distance
import pygame
from pygame.locals import *
from speech import Speech
import threading
import time

MOTOR_LEFT_EN1 = 7
MOTOR_LEFT_EN2 = 11
MOTOR_RIGHT_EN1 = 12
MOTOR_RIGHT_EN2 = 22
MOTOR_LEFT_UP = 13
MOTOR_RIGHT_UP = 16
MOTOR_LEFT_DOWN = 15
MOTOR_RIGHT_DOWN = 18

gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)
gpio.setup(MOTOR_LEFT_EN1, gpio.OUT)
gpio.setup(MOTOR_LEFT_EN2, gpio.OUT)
gpio.setup(MOTOR_RIGHT_EN1, gpio.OUT)
gpio.setup(MOTOR_RIGHT_EN2, gpio.OUT)
gpio.setup(MOTOR_LEFT_UP, gpio.OUT)
gpio.setup(MOTOR_LEFT_DOWN, gpio.OUT)
gpio.setup(MOTOR_RIGHT_UP, gpio.OUT)
gpio.setup(MOTOR_RIGHT_DOWN, gpio.OUT)

gpio.output(MOTOR_LEFT_EN1, True)
gpio.output(MOTOR_LEFT_EN2, True)
gpio.output(MOTOR_RIGHT_EN1, True)
gpio.output(MOTOR_RIGHT_EN2, True)


class PyMove:
    """
    For controlling motors by gpio raspberry and keyboard.
    """

    def __init__(self):
        self.data = []
        self.move = False

    def stop_motors(self):
        gpio.output(MOTOR_LEFT_UP, False)
        gpio.output(MOTOR_LEFT_DOWN, False)
        gpio.output(MOTOR_RIGHT_UP, False)
        gpio.output(MOTOR_RIGHT_DOWN, False)

    def distance(self):
        threading.Timer(2.0, distance).start()
        distance = Distance()
        cm = distance.distance()
        if cm <= 5.00:
            self.stop_motors()
        
        
    def start(self):
        pygame.init()
        self.distance(self)
        #pygame.mixer.init()
        #pygame.mixer.load('sounds/Processing_R2D2.mp3')
        #pygame.mixer.play(1)
        pygame.display.set_mode()
        pygame.key.set_repeat(100, 100)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
                    gpio.cleanup()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_2:
                    #pygame.mixer.music.load('sounds/Very_Excited_R2D2.mp3')
                    #pygame.mixer.music.play(1)
                    pass
                if event.type == pygame.KEYDOWN and event.key == pygame.K_3:
                    #pygame.mixer.music.load('sounds/Unbelievable_R2D2.mp3')
                    #pygame.mixer.music.play(1)
                    pass
                if event.type == pygame.KEYDOWN and event.key == pygame.K_4:
                    text = "Co jest kurwa ziomuś?"
                    speech = Speech()
                    speech.create_voice(text)
                    print text
                if event.type == pygame.KEYDOWN and event.key == pygame.K_5:
                    text = "Dawaj tutej densa"
                    speech = Speech()
                    speech.create_voice(text)
                    print text
                    gpio.output(MOTOR_LEFT_DOWN, True)
                    gpio.output(MOTOR_RIGHT_UP, True)
                    time.sleep(1)
                    gpio.output(MOTOR_LEFT_DOWN, False)
                    gpio.output(MOTOR_RIGHT_UP, False)
                    gpio.output(MOTOR_LEFT_UP, True)
                    gpio.output(MOTOR_RIGHT_DOWN, True)
                    time.sleep(1)
                    gpio.output(MOTOR_LEFT_UP, False)
                    gpio.output(MOTOR_RIGHT_DOWN, False)
                    gpio.output(MOTOR_LEFT_UP, True)
                    gpio.output(MOTOR_RIGHT_UP, True)
                    time.sleep(1)
                    gpio.output(MOTOR_LEFT_UP, False)
                    gpio.output(MOTOR_RIGHT_UP, False)
                    gpio.output(MOTOR_LEFT_DOWN, True)
                    gpio.output(MOTOR_RIGHT_DOWN, True)
                    time.sleep(1)
                    gpio.output(MOTOR_LEFT_DOWN, False)
                    gpio.output(MOTOR_RIGHT_DOWN, False)
                    
                if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                    gpio.output(MOTOR_LEFT_UP, True)
                    gpio.output(MOTOR_RIGHT_UP, True)
                elif event.type == pygame.KEYUP and event.key == pygame.K_UP:
                    text = "Up up"
                    gpio.output(MOTOR_LEFT_UP, False)
                    gpio.output(MOTOR_RIGHT_UP, False)
#                    speech = Speech()
#                    speech.create_voice(text)
    print text
if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
    text = "Down down"
    gpio.output(MOTOR_LEFT_DOWN, True)
    gpio.output(MOTOR_RIGHT_DOWN, True)
#                    speech = Speech()
#                    speech.create_voice(text)
    print text
elif event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
    text = "Down up"
    gpio.output(MOTOR_LEFT_DOWN, False)
    gpio.output(MOTOR_RIGHT_DOWN, False)
#                    speech = Speech()
#                    speech.create_voice(text)
    print text
if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
    text = "Left down"
    gpio.output(MOTOR_LEFT_DOWN, True)
    gpio.output(MOTOR_RIGHT_UP, True)
#                    speech = Speech()                
#                    speech.create_voice(text)
    print text
elif event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
    text = "Left up"
    gpio.output(MOTOR_LEFT_DOWN, False)
    gpio.output(MOTOR_RIGHT_UP, False)
#                    speech = Speech()
#                    speech.create_voice(text)
    print text
if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
    text = "Right down"
    gpio.output(MOTOR_LEFT_UP, True)
    gpio.output(MOTOR_RIGHT_DOWN, True)
#                    speech = Speech()
#                    speech.create_voice(text)
    print text
elif event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
    text = "Right up"
    gpio.output(MOTOR_LEFT_UP, False)
    gpio.output(MOTOR_RIGHT_DOWN, False)
#                    speech = Speech()
#                    speech.create_voice(text)
    print text

def create_speech(self, text):
    url_speak = "http://127.0.0.1:8000/speech?text=" + filter_spaces(text)
    response = urllib2.urlopen(url_speak)
    text = response

if __name__ == '__main__':
    PyMove().start()
