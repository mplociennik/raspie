#!/usr/bin/env python
#encoding: utf-8
import subprocess
import time

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
class Recorder():
    def record(self):
        process = subprocess.Popen("arecord -d 5 -D plughw:1,0 -f cd chunk.wav", shell=True)
        time.sleep(5.1)
        subprocess.Popen("TASKKILL /F /PID {pid} /T".format(pid=process.pid))
#        subprocess.call('arecord -D plughw:1,0 -f cd tmp/chunk.wav')
        subprocess.call('aplay chunk.wav')
        return False

if __name__ == "__main__":
    recorder = Recorder()
    recorder.record()
