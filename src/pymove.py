import pygame
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
                if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                    text = "Up down"
                    Speech.create_speech(text)
                    print text
                elif event.type == pygame.KEYUP and event.key == pygame.K_UP:
                    text = "Up up"
                    Speech.create_speech(text)
                    print text
                if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                    text = "Down down"
                    Speech.create_speech(text)
                    print text
                elif event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
                    text = "Down up"
                    Speech.create_speech(text)
                    print text
                if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                    text = "Left down"
                    Speech.create_speech(text)
                    print text
                elif event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
                    text = "Left up"
                    Speech.create_speech(text)
                    print text
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                    text = "Right down"
                    Speech.create_speech(text)
                    print text
                elif event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
                    text = "Right up"
                    Speech.create_speech(text)
                    print text

    def create_speech(self, text):
        url_speak = "http://127.0.0.1:8000/speech?text=" + filter_spaces(text)
        response = urllib2.urlopen(url_speak)
        text = response

if __name__ == '__main__':
    PyMove().start()
