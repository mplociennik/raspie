#!/usr/bin/env python
# -*- coding: utf-8 -*-
from audio import Audio
from multiprocessing import Process
from multiprocessing import Queue
import os
import pygame
from pygame.locals import *
from pymove import PyMove
from pyhead import PyHead
from speech import Speech
import subprocess
import sys
import threading
import time


class KeyControl:
    """
    For controlling motors by gpio raspberry and keyboard.
    """
    
    turn_x_ANGLE = 90
    turn_y_ANGLE = 90
    HEAD_POS_CHUNK = 15
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    font = pygame.font.SysFont('monospace', 22)
    
    def __init__(self):
        self.data = []
        pygame.key.set_repeat(100, 100)
        self.head = PyHead()
        self.move = PyMove()
        
        
    def restart_raspie(self):
        self.play_sound('sounds/Very_Excited_R2D2.mp3')
        self.run_robot_body_process('gpio_cleanup')
        python = sys.executable
        os.execl(python, python, * sys.argv)
        return

    def shutdown(self):
        self.display_text('Shutting down...')
        self.play_sound('sounds/Sad_R2D2.mp3')
        os.system("shutdown now -h")
        return

    def display_text(self, text):
#        screen_label = self.font.render(text, 1, (255, 255, 255))
#        i = 1
#        x = int(data[i * 3 + 1])
#        y = int(data[i * 3 + 2])
#        self.screen.blit(screen_label, x, y)
        print text
        return
    
    def play_sound(self, music_file):
        Audio(music_file, 1.0)
        
    def calculate_servo_position(self, angle):
#        0 stopni = 2.5
#        90 stopni = 7.5
#        180 stopni = 12.5
        duty_cycle = float(((angle / 180.0) + 1.0) * 5.0)
        return duty_cycle

    def run_robot_move_process(self, move_type):
        lock = threading.Lock()
        lock.acquire()
        try:
            getattr(self.move, move_type)()
        finally:
            lock.release()
        return False

    def run_robot_head_process(self, move_type, value):
        lock = threading.Lock()
        lock.acquire()
        try:
            getattr(self.move, move_type)(value)
        finally:
            lock.release()
        return False
        
    def autopilot_process(self, q_state):
        while True:
            self.search_free_road() 
            if not q_state.empty():
                q_state_value = q_state.get()
                if q_state_value == 'autopilot_stop':
                    print 'autopilot stop...'
                    break
                if q_state_value == 'exit':
                    print 'stoping autopilot...'
                    break
        
    def key_control(self, q_state):
        q_state.put('open')
        while True:
            if not q_state.empty():
                close = q_state.get()
                if close == 'exit':
                    print 'exiting key_control...'
                    break
                else:
                    pass
            for event in pygame.event.get():
                raise Exception('dupa')
                if event.type == pygame.KEYDOWN and event.key == pygame.K_POWER:
                    self.shutdown()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_0:
                    self.shutdown()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_9:
                    self.display_text('Restarting raspie...')
                    q_state.put('exit')
                    self.run_robot_body_process('gpio_cleanup')
                    time.sleep(2)
                    subprocess.call(['.././start.sh'])
                    sys.exit()
                if event.type == pygame.KEYUP and event.key == pygame.K_1:
                    autopilot_process = Process(target=self.autopilot_process, args=(q_state, ))
                    autopilot_process.start()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_8:
                    print 'Cleaning up gpio'
                    self.run_robot_body_process('gpio_cleanup')
                if event.type == pygame.KEYDOWN and event.key == pygame.K_2:
                    text = "Co słychać?"
                    speech = Speech()
                    speech.create_voice(text)
                    self.display_text(text)
                if event.type == pygame.KEYDOWN and event.key == pygame.K_3:
                    text = "Let's dance!"
                    speech = Speech()
                    speech.create_voice(text)
                    self.display_text(text)
                    self.run_robot_body_process('run_left_start')
                    time.sleep(1)
                    self.run_robot_body_process('run_left_stop')
                    self.run_robot_body_process('run_right_start')
                    time.sleep(1)
                    self.run_robot_body_process('run_right_stop')
                    self.run_robot_body_process('run_up_start')
                    time.sleep(1)
                    self.run_robot_body_process('run_up_stop')
                    self.run_robot_body_process('run_down_start')
                    time.sleep(1)
                    self.run_robot_body_process('run_down_stop')
                if event.type == pygame.KEYDOWN and event.key == pygame.K_4:
                    self.play_sound('sounds/Very_Excited_R2D2.mp3')
#                if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
#                    self.turn_x_ANGLE = self.turn_x_ANGLE - self.HEAD_POS_CHUNK
#                    head_pos = self.calculate_servo_position(self.turn_x_ANGLE)
#                    self.run_robot_head_process('turn_x', head_pos)
#                if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
#                    self.turn_x_ANGLE = self.turn_x_ANGLE + self.HEAD_POS_CHUNK
#                    head_pos = self.calculate_servo_position(self.turn_x_ANGLE)
#                    self.run_robot_head_process('turn_x', head_pos) 
#                if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
#                    self.display_text('Head up...')
#                    if self.turn_y_ANGLE >= 0 and self.turn_y_ANGLE <= 180:
#                        self.turn_y_ANGLE = self.turn_y_ANGLE + self.HEAD_POS_CHUNK
#                        head_pos = self.calculate_servo_position(self.turn_y_ANGLE)
#                        self.run_robot_head_process('turn_y', head_pos)
#                if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
#                    if self.turn_y_ANGLE >= 0 and self.turn_y_ANGLE <= 180:
#                        self.turn_y_ANGLE = self.turn_y_ANGLE - self.HEAD_POS_CHUNK
#                        head_pos = self.calculate_servo_position(self.turn_y_ANGLE)
#                        self.run_robot_head_process('turn_y', head_pos)                                  
                if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                    self.run_robot_body_process('run_up_start')
                elif event.type == pygame.KEYUP and event.key == pygame.K_UP:
                    self.run_robot_body_process('run_up_stop')
                if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                    self.run_robot_body_process('run_down_start')
                elif event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
                    self.run_robot_body_process('run_down_stop')
                if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                    self.run_robot_body_process('run_left_start')
                elif event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
                    self.run_robot_body_process('run_left_stop')
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                    self.run_robot_body_process('run_right_start')
                elif event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
                    self.run_robot_body_process('run_right_stop')

    def start(self):
        q_state = Queue()
        key_control = Process(target=self.key_control, args=(q_state, ))
        key_control.start()  
        
if __name__ == "__main__":
    key_control = KeyControl()
    key_control.start()
