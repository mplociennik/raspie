#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import time
import subprocess
import pygame
from pygame.locals import *
from multiprocessing
from audio import Audio
from pymove import PyMove
from autopilot import RaspieAutopilotProcess
from speech import Speech


class KeyControlProcess(multiprocessing.Process):
    """
    For controlling motors by gpio raspberry and keyboard.
    """
    
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    RUNNING_AUTOPILOT = False
    
    def __init__(self):
        multiprocessing.Process.__init__(self)
        self.exit = multiprocessing.Event()
        self.data = []
        pygame.key.set_repeat(100, 100)
        self.autopilot_process = RaspieAutopilotProcess()
        
    def restart_raspie(self):
        self.play_sound('sounds/Very_Excited_R2D2.mp3')
        python = sys.executable
        os.execl(python, python, * sys.argv)
        return

    def shutdown(self):
        self.display_text('Shutting down...')
        self.play_sound('sounds/Sad_R2D2.mp3')
        os.system("shutdown now -h")
        return

    def display_text(self, text):
        print text
        return
    
    def play_sound(self, music_file):
        audio = Audio(music_file, 1.0)
        audio_process = multiprocessing.Process(target=audio)
        audio_process.start()

    def run_autopilot(self):
        if self.autopilot_process.is_alive():
            print "Termintating..."
            self.autopilot_process.terminate()
        else:
            print "Runing autopilot!"
            self.autopilot_process.start()
        
    def key_control(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_POWER:
                self.shutdown()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_0:
                self.shutdown()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_9:
                self.display_text('Restarting raspie...')
                PyMove().gpio_cleanup()
                time.sleep(2)
                subprocess.call(['.././start.sh'])
                sys.exit()
            if event.type == pygame.KEYUP and event.key == pygame.K_1:
                self.run_autopilot()
                
                autopilot_process.start()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_8:
                print 'Cleaning up gpio'
                PyMove().gpio_cleanup()
            if event.type == pygame.KEYUP and event.key == pygame.K_2:
                text = "Good Morning! My name is Shadow. I am prototype of home asistant robot. I was programmed to listen to your commands."
                self.display_text(text)
                Speech().create_voice(text)
            if event.type == pygame.KEYUP and event.key == pygame.K_3:
                text = "Let's dance!"
                speech = Speech()
                speech.create_voice(text)
                self.display_text(text)
                PyMove().run_left_start()
                time.sleep(1)
                PyMove().run_left_stop()
                PyMove().run_right_start()
                time.sleep(1)
                PyMove().run_right_stop()
                PyMove().run_up_start()
                time.sleep(1)
                PyMove().run_up_stop()
                PyMove().run_down_start()
                time.sleep(1)
                PyMove().run_down_stop()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_4:
                self.play_sound('sounds/Very_Excited_R2D2.mp3')                               
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                PyMove().run_up_start()
            elif event.type == pygame.KEYUP and event.key == pygame.K_UP:
                PyMove().run_up_stop()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                PyMove().run_down_start()
            elif event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
                PyMove().run_down_stop()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                PyMove().run_left_start()
            elif event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
                PyMove().run_left_stop()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                PyMove().run_right_start()
            elif event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
                PyMove().run_right_stop()

    def terminate(self):
        print "Terminating autopilot..."
        self.exit.set()

    def start(self):
        while not self.exit.is_set():
            self.key_control()
        print "Key control stoped!"
        
if __name__ == "__main__":
    key_control = KeyControl()
    key_control.start()
