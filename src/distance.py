#!/usr/bin/env python2
#encoding: utf-8
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
TRIG = 31
ECHO = 32
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.output(TRIG, False)

class Distance:
    """
    For detecting distanse.
    """
    
    def __init__(self):
        pass

    def clean_gpio(self):
        GPIO.cleanup()
        
    def detect(self):
        time.sleep(0.1)
        print "Distance detection..."
        GPIO.output(TRIG,1)
        time.sleep(0.00001)
        GPIO.output(TRIG,0)
        while GPIO.input(ECHO) == 0:
            pulse_start = time.time()
        while GPIO.input(ECHO) == 1:
            pulse_stop = time.time()
        distance = (pulse_stop - pulse_start) * 17150
        distance = round(distance, 2)
        return distance

if __name__ == "__main__":
    distance = Distance()
    distance.detect()


