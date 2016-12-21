import os
import subprocess

p = subprocess.call('rec record.wav rate 32k silence 1 0.1 3% 1 3.0 3%',shell=True)
print 'recording' 
