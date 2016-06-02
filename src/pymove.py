#!/usr/bin/env python
# -*- coding: utf-8 -*-
import RPi.GPIO as gpio
import pygame
from pygame.locals import *
from speech import Speech
import time

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(7, gpio.OUT)
gpio.setup(11, gpio.OUT)
gpio.setup(13, gpio.OUT)
gpio.setup(15, gpio.OUT)

gpio.output(7, True)
gpio.output(11, True)


class PyMove:
    """
    For controlling motors by gpio raspberry and keyboard.
    """

    def __init__(self):
        self.data = []
        self.move = False

    def start(self):
        pygame.init()
        pygame.display.set_mode()
        pygame.key.set_repeat(100, 100)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_F1:
                    gpio.output(13, True)
                    gpio.output(15, False)
                    time.sleep(2)
                    gpio.output(13, False)
                    gpio.output(15, True)
                    time.sleep(2)
                    gpio.output(13, True)
                    gpio.output(15, False)
                    time.sleep(2)
                    gpio.output(13, False)
                    gpio.output(15, True)
                    time.sleep(2)
#                    text = "Cześć Sandra co tam u Ciebie?"
#                    speech = Speech()
#                    speech.create_voice(text)
#                    print text
                if event.type == pygame.KEYDOWN and event.key == pygame.K_F2:
                    text = "Sandruśku kocham Cię"
                    speech = Speech()
                    speech.create_voice(text)
                    print text
                if event.type == pygame.KEYDOWN and event.key == pygame.K_F3:
                    text = "Oliwcia co zjesz na śniadanko?"
                    speech = Speech()
                    speech.create_voice(text)
                    print text
                if event.type == pygame.KEYDOWN and event.key == pygame.K_F4:
                    text = "Co jest kurwa ziomuś?"
                    speech = Speech()
                    speech.create_voice(text)
                    print text
                if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                    text = "Up down"
                    speech = Speech()
                    speech.create_voice(text)
                    print text
                elif event.type == pygame.KEYUP and event.key == pygame.K_UP:
                    text = "Up up"
                    speech = Speech()
                    speech.create_voice(text)
                    print text
                if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                    text = "Down down"
                    speech = Speech()
                    speech.create_voice(text)
                    print text
                elif event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
                    text = "Down up"
                    speech = Speech()
                    speech.create_voice(text)
                    print text
                if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                    text = "Left down"
                    speech = Speech()                
                    speech.create_voice(text)
                    print text
                elif event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
                    text = "Left up"
                    speech = Speech()
                    speech.create_voice(text)
                    print text
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                    text = "Right down"
                    speech = Speech()
                    speech.create_voice(text)
                    print text
                elif event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
                    text = "Right up"
                    speech = Speech()
                    speech.create_voice(text)
                    print text

    def create_speech(self, text):
        url_speak = "http://127.0.0.1:8000/speech?text=" + filter_spaces(text)
        response = urllib2.urlopen(url_speak)
        text = response

if __name__ == '__main__':
    PyMove().start()
