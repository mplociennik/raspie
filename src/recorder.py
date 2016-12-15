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
        return 'Record has been saved!'


if __name__ == "__main__":
    recorder = Recorder()
    test = recorder.record()
    print test