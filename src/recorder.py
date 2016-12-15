#!/usr/bin/env python
#encoding: utf-8
import os
import signal
import subprocess
import time

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
class Recorder():
    def record(self):
        cmd = "arecord -D plughw:1,0 -f cd chunk.wav"
        time.sleep(5)
        pro = subprocess.Popen(cmd, stdout=subprocess.PIPE, 
                       shell=True, preexec_fn=os.setsid) 

        os.killpg(os.getpgid(pro.pid), signal.SIGTERM)
#        subprocess.call('arecord -D plughw:1,0 -f cd tmp/chunk.wav')
        time.sleep(0.1)
#        subprocess.call('aplay chunk.wav')
        return False

if __name__ == "__main__":
    recorder = Recorder()
    recorder.record()
