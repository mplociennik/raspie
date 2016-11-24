import os
import sys
import time
import pyvona

IVONA_ACCESS_KEY = 'GDNAIKZKKGPM3SPFPZGA'
IVONA_SECRET_KEY = 'PXnXmq3aV1qYsV4jxG4WtoVhESq4gZaXGjrDTBke'

name = 'Joey'
region = 'eu-east'
text = "Witaj, jestem Raspi Bot. Asystent pok³adowy Ju Es Es Enterprajs"
v = pyvona.create_voice(IVONA_ACCESS_KEY, IVONA_SECRET_KEY)
v.voice_name = name
v.region = region
try:
    v.fetch_voice(text, 'voice_file')
except:
    print "Speech: connection not found!"
    
time.sleep(0.001)
os.system('play voice_file.ogg stretch 1.2 133.33 lin 0.2 0.4 \
overdrive 30 30 echo 0.4 0.8 15 0.8 \
synth sine fmod 30 echo 0.8 0.8 29 0.8')
