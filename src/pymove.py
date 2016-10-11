#!/usr/bin/env python
# -*- coding: utf-8 -*-
import RPi.GPIO as gpio
from distance import Distance
import pygame
from pygame.locals import *
from speech import Speech
import multiprocessing
import time
import os


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
        self.autopilot = False;
        self.obstacle = False;
        pygame.init()
        self.screen = pygame.display.set_mode()
        pygame.key.set_repeat(100, 100)
        self.font = pygame.font.SysFont('monospace', 22)

    def stop_motors(self):
        self.display_text('stoping motors...')
        gpio.output(MOTOR_LEFT_UP, False)
        gpio.output(MOTOR_LEFT_DOWN, False)
        gpio.output(MOTOR_RIGHT_UP, False)
        gpio.output(MOTOR_RIGHT_DOWN, False)

    def distance(self):
        distance = Distance()
        cm = distance.detect()
        if cm <= 10:
            self.obstacle = True
            self.stop_motors()
        
    def autopilot(self):
        while True:
            if self.autopilot:
                speech.play_sound('sounds/Very_Excited_R2D2.mp3')
                self.display_text('Autopilot starting...')
                if self.obstacle:
                    speech.play_sound()
                    gpio.output(MOTOR_LEFT_UP, True)
                    gpio.output(MOTOR_RIGHT_DOWN, True)
                    time.sleep(1)
                    gpio.output(MOTOR_LEFT_UP, False)
                    gpio.output(MOTOR_RIGHT_DOWN, False)
                else:
                    gpio.output(MOTOR_LEFT_UP, True)
                    gpio.output(MOTOR_RIGHT_UP, True)
            time.sleep(1)

    def restart_raspie(self):
        speech.play_sound('sounds/Very_Excited_R2D2.mp3')
        gpio.cleanup()
        python = sys.executable
        os.execl(python, python, * sys.argv)

    def shutdown(self):
        self.display_text('Shutting down...')
        speech.play_sound('sounds/Sad_R2D2.mp3')
        os.system("shutdown now -h")

    def display_text(self, text):
#        label = self.font.render(text, 1, (255,255,0))
#        self.screen.blit(label, 100,100)
        print text
        return True

    def run_up_start(self):
        text = "UP Start"
        self.display_text(text)
        gpio.output(MOTOR_LEFT_UP, True)
        gpio.output(MOTOR_RIGHT_UP, True)

    def run_up_stop(self):
        text = "UP Stop"
        self.display_text(text)
        gpio.output(MOTOR_LEFT_UP, False)
        gpio.output(MOTOR_RIGHT_UP, False)

    def run_down_start(self):
        text = "DOWN Start"
        self.display_text(text)
        gpio.output(MOTOR_LEFT_DOWN, True)
        gpio.output(MOTOR_RIGHT_DOWN, True)

    def run_down_stop():
        text = "DOWN Stop"
        self.display_text(text)
        gpio.output(MOTOR_LEFT_DOWN, False)
        gpio.output(MOTOR_RIGHT_DOWN, False)

    def run_left_start():
        text = "LEFT Start"
        self.display_text(text)
        gpio.output(MOTOR_LEFT_DOWN, True)
        gpio.output(MOTOR_RIGHT_UP, True)

    def run_left_stop():
        text = "LEFT Stop"
        self.display_text(text)
        gpio.output(MOTOR_LEFT_DOWN, False)
        gpio.output(MOTOR_RIGHT_UP, False)

    def run_right_start():
        text = "RIGHT Start"
        self.display_text(text)
        gpio.output(MOTOR_LEFT_UP, True)
        gpio.output(MOTOR_RIGHT_DOWN, True)

    def run_right_stop():
        text = "RIGHT Stop"
        self.display_text(text)
        gpio.output(MOTOR_LEFT_UP, False)
        gpio.output(MOTOR_RIGHT_DOWN, False)
        
    def key_control(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_POWER:
                    self.shutdown()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
                    self.display_text('Restarting raspie...')
                    self.restart_raspie()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_2:
                    if(self.autopilot):
                        text = 'Stoping autopilot...'
                        self.autopilot = False
                    else:
                        text = 'Starting autopilot...'
                        self.autopilot = True
                    self.display_text(text)
                if event.type == pygame.KEYDOWN and event.key == pygame.K_3:
                    pass
                if event.type == pygame.KEYDOWN and event.key == pygame.K_4:
                    text = "Co słychać?"
                    speech = Speech()
                    speech.create_voice(text)
                    self.display_text(text)
                if event.type == pygame.KEYDOWN and event.key == pygame.K_5:
                    text = "Let's dance!"
                    speech = Speech()
                    speech.create_voice(text)
                    self.display_text(text)
                    self.run_left_start()
                    time.sleep(1)
                    self.run_left_stop()
                    self.run_right_start()
                    time.sleep(1)
                    self.run_right_stop()
                    self.run_up_start()
                    time.sleep(1)
                    self.run_up_stop()
                    self.run_down_start()
                    time.sleep(1)
                    self.run_down_stop()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                    self.run_up_start()
                elif event.type == pygame.KEYUP and event.key == pygame.K_UP:
                    self.run_up_stop()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                    self.run_down_start()
                elif event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
                    self.run_down_stop()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                    self.run_left_start()
                elif event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
                    self.run_left_stop()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                    self.run_right_start()
                elif event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
                    self.run_right_stop()

    def create_speech(self, text):
        url_speak = "http://127.0.0.1:8000/speech?text=" + filter_spaces(text)
        response = urllib2.urlopen(url_speak)
        text = response

    def start(self):
        jobs = []
        key_control = multiprocessing.Process(target=self.key_control)
        autopilot = multiprocessing.Process(target=self.autopilot)
        distance = multiprocessing.Process(target=self.distance)

        jobs.append(distance)
        jobs.append(key_control)
        jobs.append(autopilot)

        distance.start()
        key_control.start()
        autopilot.start()


if __name__ == '__main__':
    PyMove().start()
