#! /usr/bin/python3.4
# _*_coding:utf-8_*_

import os
import wave

class GetVoiceData(object):

    def __init__(self):
        
        self.filename = "samples.wav"

    def get_voice(self):
        
        print("Start recording :")
        os.system('arecord -D "plughw:1,0" -f S16_LE -d 5 -r 16000 {}'.format(self.filename))
        print("Done!")
        
    def get_data(self):

        wf = open(self.filename,"rb")
        voice_data = wf.read()
        wf.close

        return voice_data

m = GetVoiceData()
m.get_voice()
