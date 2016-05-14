import os
import pygame
from pygame.locals import *
import time
import urllib2


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
                if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                    text = "Up down"
                    self.create_speech(text)
                    print text
                elif event.type == pygame.KEYUP and event.key == pygame.K_UP:
                    text = "Up up"
                    self.create_speech(text)
                    print text
                if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                    text = "Down down"
                    self.create_speech(text)
                    print text
                elif event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
                    text = "Down up"
                    self.create_speech(text)
                    print text
                if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                    text = "Left down"
                    self.create_speech(text)
                    print text
                elif event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
                    text = "Left up"
                    self.create_speech(text)
                    print text
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                    text = "Right down"
                    self.create_speech(text)
                    print text
                elif event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
                    text = "Right up"
                    self.create_speech(text)
                    print text
                    
    def filter_spaces(self, text):
        return text.replace(" ", "%20")

    def create_speech(self, text):
        url_speak = "http://127.0.0.1:8000/speech?text=" + filter_spaces(text)
        response = urllib2.urlopen(url_speak)
        text = response

if __name__ == '__main__':
    PyMove().start()
