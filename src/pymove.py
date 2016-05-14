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
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                    print "Up down"
                elif event.type == pygame.KEYUP and event.key == pygame.K_UP:
                    print "Up up"
                if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                    print "Down down"
                elif event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
                    print "Down up"
                if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                    print "Left down"
                elif event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
                    print "Left up"
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                    print "Right down"
                elif event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
                    print "Right up"

if __name__ == '__main__':
    PyMove().start()
