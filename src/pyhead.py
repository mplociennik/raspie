#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import RPi.GPIO as gpio

# Head init configuration
SERVO_X = 13
SERVO_Y = 12

gpio.setup(SERVO_X, gpio.OUT)
gpio.setup(SERVO_Y, gpio.OUT)
pwm_X = gpio.PWM(SERVO_X, 50)
pwm_Y = gpio.PWM(SERVO_Y, 50)

class PyHead():
    """
    For controlling servo head.
    need analyze:
    http://abyz.co.uk/rpi/pigpio/python.html
    https://github.com/richardghirst/PiBits/tree/master/ServoBlaster
    """
    def __init__(self):
        self.data = []
        pwm_X.start(7.5)
        pwm_Y.start(7.5)
        time.sleep(1)
        pwm_X.stop()
        pwm_Y.stop()

    
    def gpio_cleanup(self):
        gpio.cleanup()
        return

    def turn_x(self, pos): 
        if pos >= 2.5 and pos <=12.5:
            print "turning pos X to: {0}".format(pos)
            pwm_X.start(pos)
            time.sleep(0.2)
            pwm_X.stop()
        else:
            print "Position X out of range: {0}".format(pos)

    def turn_y(self, pos):
        if pos >= 2.5 and pos <=12.5:
            print "turning pos Y to: {0}".format(pos)
            pwm_Y.start(7.5)
            time.sleep(0.2)
            pwm_Y.stop()
        else:
            print "Position out of range: {0}".format(pos)

    def test(self):
        while True:
            self.turn_x(2.5)
            self.turn_y(2.5)
            time.sleep(1)
            self.turn_x(7.5)
            self.turn_y(7.5)
            time.sleep(1)
            self.turn_x(12.5)
            self.turn_y(12.5)
            time.sleep(1)
        
if __name__ == '__main__':
    head = PyHead
    head.autopilot_process()
