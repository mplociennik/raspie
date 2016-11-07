#!/usr/bin/env python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
''' http://makezine.com/projects/raspberry-eye-remote-servo-cam/ sprawdzic'''

GPIO.setmode(GPIO.BCM)
GPIO.setup(7, GPIO.OUT)
pwm = GPIO.PWM(7, 50)
pwm.start(7.5)

try:
    while True:
        pwm.changeDutyCycle(7.5)
        time.sleep(1)
        pwm.changeDutyCycle(12.5)
        time.sleep(1)
        pwm.changeDutyCycle(2.5)
        time.sleep(1)
except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()