#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import RPi.GPIO as gpio
from distance import Distance

gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)

# Motors init configuration
MOTOR_RIGHT_EN1 = 7
MOTOR_RIGHT_EN2 = 11
MOTOR_LEFT_EN1 = 12
MOTOR_LEFT_EN2 = 22
MOTOR_RIGHT_DOWN = 13
MOTOR_LEFT_DOWN = 16
MOTOR_RIGHT_UP = 15
MOTOR_LEFT_UP = 18

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

# Head init configuration
SERVO_X = 13
SERVO_Y = 12

gpio.setup(SERVO_X, gpio.OUT)
pwm_X = gpio.PWM(SERVO_X, 50)
pwm_X.start(7.5)

gpio.setup(SERVO_Y, gpio.OUT)
pwm_Y = gpio.PWM(SERVO_Y, 50)
pwm_Y.start(7.5)


class PyMove():
    """
    For controlling motors by gpio raspberry and keyboard.
    """
    def __init__(self):
        self.data = []
    
    def gpio_cleanup(self):
        gpio.cleanup()
        return
    
    def display_text(self, text):
#        label = self.font.render(text, 1, (255,255,0))
#        self.screen.blit(label, 100,100)
        print text
        return 
    
    def stop_motors(self):
        self.display_text('stoping motors...')
        gpio.output(MOTOR_LEFT_UP, False)
        gpio.output(MOTOR_LEFT_DOWN, False)
        gpio.output(MOTOR_RIGHT_UP, False)
        gpio.output(MOTOR_RIGHT_DOWN, False)   
        self.display_text('stoped!')

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
        
    def search_free_road(self):
        text = 'Looking for free road...'
        self.display_text(text)
        distance = Distance()
        cm = distance.detect()
        self.display_text('Distance:')
        self.display_text(cm)
        print int(cm)
        if int(cm) <= 30:
            self.display_text('Obstacle!')
            self.play_sound('sounds/Processing_R2D2.mp3')
            self.stop_motors()
            time.sleep(1)
            self.run_down_start()
            time.sleep(0.3)
            self.run_down_stop()
            time.sleep(0.3)
            self.run_right_start()
            time.sleep(0.3)
            self.run_right_stop()
            print 'end obstacle'
            self.search_free_road()
        else:
            self.display_text('run!')
            self.run_up_start()
        
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

    def head_x(self, pos): 
        print "chaging pos to: {0}".format(pos)
        pwm_X.ChangeDutyCycle(pos)        

    def head_y(self, pos):
        print "chaging pos to: {0}".format(pos)
        pwm_Y.ChangeDutyCycle(pos)    
        
if __name__ == '__main__':
    move = PyMove
    move.autopilot_process()
