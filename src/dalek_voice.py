import os
import sys
import time

os.system('say -v Albert -o exterminate.aiff --data-format=BEI16@44100 \
exterminate, exterminate, exterminate!')
time.sleep(0.001)
os.system('play exterminate.aiff stretch 1.2 133.33 lin 0.2 0.4 \
overdrive 30 30 echo 0.4 0.8 15 0.8 \
synth sine fmod 30 echo 0.8 0.8 29 0.8')
