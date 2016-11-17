#!/usr/bin/env python2
#encoding: utf-8
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
TRIG = 3
ECHO = 5
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
        try:
            print "start"
            time.sleep(1)
            GPIO.output(TRIG,1)
            time.sleep(0.000001)
            GPIO.output(TRIG,0)
            time.sleep(0.000001)
            print GPIO.input(ECHO)
            while GPIO.input(ECHO) == False:
                print "start"
                print GPIO.input(ECHO)
                pulse_start = time.time()
            while GPIO.input(ECHO) == True:
                print GPIO.input(ECHO)
                pulse_stop = time.time()               
            distance = (pulse_stop - pulse_start) * 17150
            distance = round(distance, 2)
            return distance
        except KeyboardInterrupt:
            print "interrupt"
        finally:
            GPIO.cleanup()

if __name__ == "__main__":
    distance = Distance()
    print 'distance: {0} cm'.format(distance.detect())


