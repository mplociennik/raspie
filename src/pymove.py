import pygame


class PyMove:
    """
    For controlling motors by gpio raspberry and keyboard.
    """

    def __init__(self):
        self.data = []

    def start(self):
        while 1:
            screen.fill(0)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == K_w:
                        #keys[0]=True
                        print "K up"
                if event.type == pygame.KEYUP:
                    if event.key == K_w:
                        keys[0]=True
                        print "K up"
