#!/usr/bin/env python
# -*- coding: utf-8 -*-
import RPi.GPIO as gpio
import pygame
from pygame.locals import *
from speech import Speech
import time

gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)
gpio.setup(7, gpio.OUT)
gpio.setup(11, gpio.OUT)
gpio.setup(12, gpio.OUT)
gpio.setup(22, gpio.OUT)
gpio.setup(13, gpio.OUT)
gpio.setup(15, gpio.OUT)
gpio.setup(16, gpio.OUT)
gpio.setup(18, gpio.OUT)

gpio.output(7, True)
gpio.output(11, True)
gpio.output(12, True)
gpio.output(22, True)


class PyMove:
    """
    For controlling motors by gpio raspberry and keyboard.
    """

    def __init__(self):
        self.data = []
        self.move = False

    def start(self):
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_mode()
        pygame.key.set_repeat(100, 100)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
                    gpio.cleanup()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_2:
                    pygame.mixer.music.load('sounds/Very_Excited_R2D2.mp3')
                    pygame.mixer.music.play(1)
                if event.type == pygame.KEYDOWN and event.key == pygame.K_3:
                    pygame.mixer.music.load('sounds/Unbelievable_R2D2.mp3')
                    pygame.mixer.music.play(1)
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
                    gpio.output(15, True)
                    gpio.output(16, True)
                    time.sleep(1)
                    gpio.output(15, False)
                    gpio.output(16, False)
                    gpio.output(13, True)
                    gpio.output(18, True)
                    time.sleep(1)
                    gpio.output(13, False)
                    gpio.output(18, False)
                    gpio.output(13, True)
                    gpio.output(16, True)
                    time.sleep(1)
                    gpio.output(13, False)
                    gpio.output(16, False)
                    gpio.output(15, True)
                    gpio.output(18, True)
                    time.sleep(1)
                    gpio.output(15, False)
                    gpio.output(18, False)
                    
                if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                    gpio.output(13, True)
                    gpio.output(16, True)
                elif event.type == pygame.KEYUP and event.key == pygame.K_UP:
                    text = "Up up"
                    gpio.output(13, False)
                    gpio.output(16, False)
#                    speech = Speech()
#                    speech.create_voice(text)
                    print text
                if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                    text = "Down down"
                    gpio.output(15, True)
                    gpio.output(18, True)
#                    speech = Speech()
#                    speech.create_voice(text)
                    print text
                elif event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
                    text = "Down up"
                    gpio.output(15, False)
                    gpio.output(18, False)
#                    speech = Speech()
#                    speech.create_voice(text)
                    print text
                if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                    text = "Left down"
                    gpio.output(15, True)
                    gpio.output(16, True)
#                    speech = Speech()                
#                    speech.create_voice(text)
                    print text
                elif event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
                    text = "Left up"
                    gpio.output(15, False)
                    gpio.output(16, False)
#                    speech = Speech()
#                    speech.create_voice(text)
                    print text
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                    text = "Right down"
                    gpio.output(13, True)
                    gpio.output(18, True)
#                    speech = Speech()
#                    speech.create_voice(text)
                    print text
                elif event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
                    text = "Right up"
                    gpio.output(13, False)
                    gpio.output(18, False)
#                    speech = Speech()
#                    speech.create_voice(text)
                    print text

    def create_speech(self, text):
        url_speak = "http://127.0.0.1:8000/speech?text=" + filter_spaces(text)
        response = urllib2.urlopen(url_speak)
        text = response

if __name__ == '__main__':
    PyMove().start()
