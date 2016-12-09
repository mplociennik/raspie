#!/usr/bin/env python
#encoding: utf-8
import subprocess
import time

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
class Recorder():
    def record(self):
        p = subprocess.Popen("arecord -D plughw:1,0 -d 2 -f cd tmp/chunk.wav", shell=True)
        time.sleep(2)
        p.kill()
#        subprocess.call('arecord -D plughw:1,0 -f cd tmp/chunk.wav')
        subprocess.call('aplay tmp/chunk.wav')
        return False

if __name__ == "__main__":
    recorder = Recorder()
    recorder.record()
