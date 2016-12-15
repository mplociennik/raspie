#!/usr/bin/env python
#encoding: utf-8
import os
import signal
import subprocess
import time


class Recorder():
    def record(self):
        cmd = "arecord -D plughw:1,0 -f cd chunk.wav"
        pro = subprocess.Popen(cmd, stdout=subprocess.PIPE, 
                       shell=True, preexec_fn=os.setsid) 
        time.sleep(5)
        os.killpg(os.getpgid(pro.pid), signal.SIGTERM)
        time.sleep(0.1)
        subprocess.call('aplay chunk.wav')
        return False


if __name__ == "__main__":
    recorder = Recorder()
    recorder.record()
