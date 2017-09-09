#! usr/bin/python3.4
# _*_coding:utf-8_*_

import os
import json

import base64

import numpy as np
from datetime import datetime

from urllib.request import urlopen,Request
from urllib.error import URLError
from urllib.parse import urlencode

class GetVoiceData(object):

    def __init__(self):
        
        self.filename = "null_data.wav"

    def get_voice(self):
        
        print("Start recording :")
        os.system('arecord -D "plughw:1,0" -f S16_LE -d 5 -r 16000 {}'.format(self.filename))
        print("Done!")

        wf = open(self.filename,"rb")
        voice_data = wf.read()
        wf.close
        
        return voice_data

if __name__ == "__main__":

    save_count = 0
    save_buffer = []  
    for i in range(0,1):
        
        now = datetime.now()
        print(now)
        voice_filename = "{}.wav".format(now.minute)
        
        voice = GetVoiceData()
        voice_data = voice.get_voice()

        # print(len(voice_data))
        # print(type(voice_data))

        audio_data = np.fromstring(voice_data,dtype = np.short)
        print(audio_data)
        audio_data.shape = -1,1
        print(audio_data)

        audio_data = audio_data.T
        print(audio_data)
        
        time = np.arange(0,len(audio_data)) * (1.0/8000)

        print(time)
        
        
        
        
    
