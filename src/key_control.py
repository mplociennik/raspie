#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
import subprocess
from multiprocessing import Process, Queue
from pygame.locals import *
from speech import Speech
from audio import Audio
from pymove import PyMove as move


class KeyControl:
    """
    For controlling motors by gpio raspberry and keyboard.
    """
    def __init__(self):
        self.data = []
        pygame.init()
        self.screen = pygame.display.set_mode()
        pygame.key.set_repeat(100, 100)
        self.font = pygame.font.SysFont('monospace', 22)

    def restart_raspie(self):
        self.play_sound('sounds/Very_Excited_R2D2.mp3')
        move.gpio_cleanup()
        python = sys.executable
        os.execl(python, python, * sys.argv)

    def shutdown(self):
        self.display_text('Shutting down...')
        self.play_sound('sounds/Sad_R2D2.mp3')
        os.system("shutdown now -h")

    def display_text(self, text):
#        label = self.font.render(text, 1, (255,255,0))
#        self.screen.blit(label, 100,100)
        print text
        return 
    
    def play_sound(self, music_file):
        Audio(music_file, 1.0)
        
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
                if event.type == pygame.KEYDOWN and event.key == pygame.K_POWER:
                    self.shutdown()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_0:
                    self.shutdown()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_9:
                    self.display_text('Restarting raspie...')
                    q_state.put('exit')
                    move.gpio_cleanup()
                    time.sleep(2)
                    subprocess.call(['.././start.sh'])
                    sys.exit()
                if event.type == pygame.KEYUP and event.key == pygame.K_1:
                    autopilot_process = Process(target=self.autopilot_process, args=(q_state,))
                    autopilot_process.start()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_8:
                    print 'Cleaning up gpio'
                    move.gpio_cleanup()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_2:
                    text = "Co słychać?"
                    speech = Speech()
                    speech.create_voice(text)
                    self.display_text(text)
                if event.type == pygame.KEYDOWN and event.key == pygame.K_3:
                    self.play_sound('sounds/Very_Excited_R2D2.mp3')
                    text = "Let's dance!"
                    speech = Speech()
                    speech.create_voice(text)
                    self.display_text(text)
                    move.run_left_start()
                    time.sleep(1)
                    move.run_left_stop()
                    main.run_right_start()
                    time.sleep(1)
                    main.run_right_stop()
                    main.run_up_start()
                    time.sleep(1)
                    main.run_up_stop()
                    main.run_down_start()
                    time.sleep(1)
                    main.run_down_stop()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_4:
                    self.play_sound('sounds/Very_Excited_R2D2.mp3')
                if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                    main.run_up_start()
                elif event.type == pygame.KEYUP and event.key == pygame.K_UP:
                    main.run_up_stop()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                    main.run_down_start()
                elif event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
                    main.run_down_stop()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                    move.run_left_start()
                elif event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
                    move.run_left_stop()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                    main.run_right_start()
                elif event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
                    main.run_right_stop()

    def start(self):
        q_state = Queue()
        key_control = Process(target=self.key_control, args=(q_state,))
        key_control.start()  
        
if __name__ == "__main__":
    key_control = KeyControl()
    key_control.start()
