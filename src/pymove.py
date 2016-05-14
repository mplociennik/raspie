#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from speech import Speech
from pygame.locals import *


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
                    text = "Cześć Sandra co tam u Ciebie?"
                    speech = Speech()
                    speech.create_voice(text)
                    print text
                elif event.type == pygame.KEYUP and event.key == pygame.K_UP:
                    text = "F jeden up"
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
