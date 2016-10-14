#!/usr/bin/env python
# -*- coding: utf-8 -*-
import RPi.GPIO as gpio
from distance import Distance
import pygame
from pygame.locals import *
from speech import Speech
from multiprocessing import Process, Queue
import time
import os
import sys


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
        self.display_text('stoped!')

    def restart_raspie(self):
        speech = Speech()
        speech.play_sound('sounds/Very_Excited_R2D2.mp3')
        gpio.cleanup()
        python = sys.executable
        os.execl(python, python, * sys.argv)

    def shutdown(self):
        self.display_text('Shutting down...')
        speech = Speech()
        speech.play_sound('sounds/Sad_R2D2.mp3')
        os.system("shutdown now -h")

    def display_text(self, text):
#        label = self.font.render(text, 1, (255,255,0))
#        self.screen.blit(label, 100,100)
        print text
        return False

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

    def run_down_stop(self):
        text = "DOWN Stop"
        self.display_text(text)
        gpio.output(MOTOR_LEFT_DOWN, False)
        gpio.output(MOTOR_RIGHT_DOWN, False)

    def run_left_start(self):
        text = "LEFT Start"
        self.display_text(text)
        gpio.output(MOTOR_LEFT_DOWN, True)
        gpio.output(MOTOR_RIGHT_UP, True)

    def run_left_stop(self):
        text = "LEFT Stop"
        self.display_text(text)
        gpio.output(MOTOR_LEFT_DOWN, False)
        gpio.output(MOTOR_RIGHT_UP, False)

    def run_right_start(self):
        text = "RIGHT Start"
        self.display_text(text)
        gpio.output(MOTOR_LEFT_UP, True)
        gpio.output(MOTOR_RIGHT_DOWN, True)

    def run_right_stop(self):
        text = "RIGHT Stop"
        self.display_text(text)
        gpio.output(MOTOR_LEFT_UP, False)
        gpio.output(MOTOR_RIGHT_DOWN, False)
        
    def autopilot_process(self, q_state):
        while True:
            distance = Distance()
            cm = distance.detect()
            self.display_text('Distance:')
            self.display_text(cm)
            print int(cm)
            if int(cm) <= 20:
                self.display_text('Obstacle!')
                self.stop_motors()
                time.sleep(1)
                self.run_right_start()
                time.sleep(1)
                self.run_right_stop()
                print 'end obstacle'
            else:
                self.display_text('run!')
                self.run_up_start()
                
            if not q_state.empty():
                exit = q_state.get()
                if exit == 'exit' or exit == 'autopilot_stop':
                    print 'stoping autopilot...'
                    break
            
    def key_control(self, q_state):
        q_state.put('open')
        while True:
            if not close_program.empty():
                close = q_state.get()
                if close == 'exit':
                    print 'exiting key_control...'
                    break
                else:
                    pass
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_POWER:
                    self.shutdown()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
                    self.display_text('Closing raspie...')
                    q_state.put('exit')
                    gpio.cleanup()
                    time.sleep(2)
                    sys.exit()
                if event.type == pygame.KEYUP and event.key == pygame.K_2:
                    if q_state.get() == 'autopilot_stop':
                        autopilot_process = Process(target=self.autopilot_process, args=(self.q_state,))
                        autopilot_process.start()
                        q_state.put('autopilot_start')
                    else:
                        q_state.put('autopilot_stop')
                        
                if event.type == pygame.KEYDOWN and event.key == pygame.K_3:
                    print 'Cleaning up gpio'
                    gpio.cleanup()
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
        q_state = Queue()
        key_control = Process(target=self.key_control, args=(self.q_state,))
        key_control.start()
        

if __name__ == '__main__':
    PyMove().start()
