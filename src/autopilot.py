#!/usr/bin/env python
# -*- coding: utf-8 -*-
import multiprocessing
import time
from pymove import PyMove


class RaspieAutopilotProcess(multiprocessing.Process):

    DIST_TOLERANCE = 2
    def __init__(self, ):
        multiprocessing.Process.__init__(self)
        self.exit = multiprocessing.Event()
        
    def detect_no_movement(self, now_distance, last_distance):
        sub = now_distance - last_distance
        return sub <= self.DIST_TOLERANCE
        
    def search_free_road(self, last_distance=None):
        text = 'Looking for free road...'
        self.display_text(text)
        distance = Distance()
        cm = distance.detect()
        print int(cm)
        if last_distance is not None:
            if self.detect_no_movement(int(cm), last_distance):
                self.search_free_road(int(cm))
        if int(cm) <= 30:
            print "Obstacle!"
            self.stop_motors()
            time.sleep(1)
            self.run_down_start()
            time.sleep(0.3)
            self.run_down_stop()
            time.sleep(0.3)
            self.run_right_start()
            time.sleep(0.3)
            self.run_right_stop()
            self.search_free_road(last_distance)
        else:
            print "Run!"
            PyMove().run_up_start()
            
    def start(self):
        while not self.exit.is_set():
            self.search_free_road()
        print "Autopilot stoped!"

    def terminate(self):
        print "Terminating autopilot..."
        self.exit.set()


if __name__ == "__main__":
    process = RaspieAutopilotProcess()
    process.start()
    print "Waiting for a while"
    time.sleep(3)
    process.terminate()
    time.sleep(3)
    print "Child process state: %d" % process.is_alive()