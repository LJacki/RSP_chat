#! /usr/bin/python3.4
# _*_coding:utf-8_*_

import json
import base64

from urllib.request import urlopen,Request
from urllib.error import URLError
from urllib.parse import urlencode

CU_ID = "28-D2-44-44-67-B9"
API_KEY = "76723YF5OUIkBgW9iyDb9DPW"
API_SECRET = "392c0282fd778dbd3d75051673ffa19b"

class GetToken(object):

    def __init__(self):

        self.api_key = API_KEY
        self.api_secret = API_SECRET
        self.tokenUrl = "https://openapi.baidu.com/oauth/2.0/token"


    def get_token(self):
        tokenData = {
                    'grant_type': 'client_credentials',
                    'client_id': self.api_key,
                    'client_secret': self.api_secret,
                    }

        response = urlopen(self.tokenUrl,
                           data=bytes(urlencode(tokenData),
                                      encoding = 'utf-8'))

        response_text = response.read().decode("utf-8")
        json_result = json.loads(response_text)
        return json_result['access_token']

class SoundToText(object):

    def __init__(self, language = "zh"):

        self.language = language
        self.token =  GetToken().get_token()
        self.rate = 16000
        self.cu_id = CU_ID

        self.stt_url = "http://vop.baidu.com/server_api"

    # def voice_to_data(self):

    def get_text_data(self,voice_data):
        sttUrlData = dict(
            format = 'wav',
            lan = self.language,
            token = self.token,
            len = len(voice_data),
            rate = self.rate,
            speech = base64.b64encode(voice_data).decode('utf-8'),
            cuid = self.cu_id,
            channel = 1,
        )

        post_data = json.dumps(sttUrlData)
        self.request = Request(self.stt_url,
                               data=bytes(post_data,
                                          encoding='utf-8'))

        try:
            w_data = urlopen(self.request)
            # print("this w_data:",w_data)
        except URLError:
            raise IndexError("No internet connection available to transfer audio data")

        except:
            raise KeyError("Server wouldn't respond (invalid key or quota has been maxed out)")

        response_text = w_data.read().decode('utf-8')
        #print("response_text",response_text)
        json_result = json.loads(response_text)

        if int(json_result['err_no']) != 0:
            raise LookupError(json_result['err_msg'])
        else:
            print(json_result['result'][0])
            return json_result['result'][0]


if __name__ == "__main__":
    
    fs = open("samples.wav",'rb')
    voice_data = fs.read()
    fs.close()

    for i in range(0,100):
        

        stt = SoundToText()
        result = stt.get_text_data(voice_data)
        # print (result)
        i += 1
        
