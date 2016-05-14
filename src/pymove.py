import pygame
from pygame.locals import *


class PyMove:
    """
    For controlling motors by gpio raspberry and keyboard.
    """

    def __init__(self):
        self.data = []
        self.move = false

    def start(self):
        pygame.init()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
                    print "dupa down"
                elif event.type == pygame.KEYUP and event.key == pygame.K_d:
                    print "dupa up"

if __name__ == '__main__':
    PyMove().start()
