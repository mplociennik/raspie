#!/usr/bin/env python
#encoding: utf-8
import os
import subprocess


class Recorder():
    def record(self):
        command = 'rec record.wav rate 32k silence 1 0.1 3% 1 3.0 3'
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
        process.wait()
        print process.returncode
#        p = subprocess.call('rec record.wav rate 32k silence 1 0.1 3% 1 3.0 3%',shell=True)


if __name__ == "__main__":
    recorder = Recorder()
    recorder.record()