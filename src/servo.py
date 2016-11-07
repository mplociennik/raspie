#!/usr/bin/env python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
''' http://makezine.com/projects/raspberry-eye-remote-servo-cam/ sprawdzic'''
SERVO_Y = 33
SERVO_X = 35
GPIO.setmode(GPIO.BOARD)
GPIO.setup(SERVO_Y, GPIO.OUT)
pwm_Y = GPIO.PWM(SERVO_Y, 50)
pwmY.start(7.5)
GPIO.setup(SERVO_X, GPIO.OUT)
pwm_X = GPIO.PWM(SERVO_Y, 50)
pwm_X.start(7.5)

try:
    while True:
        print "cycle..."
        pwm_Y.ChangeDutyCycle(7.5)
        pwm_X.ChangeDutyCycle(7.5)
        time.sleep(1)
        pwm_Y.ChangeDutyCycle(12.5)
        pwm_X.ChangeDutyCycle(12.5)
        time.sleep(1)
        pwm._Y.ChangeDutyCycle(2.5)
        pwm._X.ChangeDutyCycle(2.5)
        time.sleep(1)
except KeyboardInterrupt:
    pwm_Y.stop()
    pwm_X.stop()
    GPIO.cleanup()
