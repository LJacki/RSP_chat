#! /usr/bin/python3
# _*_ encoding:utf-8_*_

import json
import base64

from urllib.request import urlopen,Request
from urllib.error import URLError
from urllib.parse import urlencode

# CU_ID是用户标识，随便定义，一般为设备MAC地址
# 这里在使用时换成自己申请的 API_KEY 和对应的API_SECRET
CU_ID = "88-88-88-88-88-88-88"
API_KEY = "76723YF5OUIkBgW988888888"
API_SECRET = "392c0282fd778dbd3d75051688888888"

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

        response = urlopen(self.tokenUrl,data=bytes(urlencode(tokenData),encoding = 'utf-8'))

        response_text = response.read().decode("utf-8")
        json_result = json.loads(response_text)
        return json_result['access_token']

class TextToSpeech(object):

    def __init__(self,language = "zh"):
        self.cu_id = CU_ID
        # self.api_key = API_KEY
        # self.api_secret = API_SECRET
        self.language = language

        self.token = GetToken().get_token()
        self.tts_url = "http://tsn.baidu.com/text2audio" # ?tex=%s&lan=zh&cuid=%s&ctp=1&tok=%s"

    def get_wave_data(self,text):

        if len(text) >1024:
            raise KeyError("Text length must less than 1024 bytes")

        ttsUrlData =dict(
            tex = text,
            lan = self.language,
            tok = self.token,
            ctp = 1,
            cuid = self.cu_id,
            spd = 4,
            pit = 5,
            vol = 5,
            per = 0,
        )
        """
        tex	必填	合成的文本，使用UTF-8编码，请注意文本长度必须小于1024字节
        lan	必填	语言选择,填写zh
        tok	必填	开放平台获取到的开发者 access_token
        ctp	必填	客户端类型选择，web端填写1
        cuid必填	用户唯一标识，用来区分用户，填写机器 MAC 地址或 IMEI 码，长度为60以内
        spd	选填	语速，取值0-9，默认为5中语速
        vol	选填	音量，取值0-9，默认为5中音量
        per	选填	发音人选择, 0为女声，1为男声，3为情感合成-度逍遥，4为情感合成-度丫丫，默认为普通女声
        """
        self.request = Request(self.tts_url,data = bytes(urlencode(ttsUrlData),encoding='utf-8'))

        # check error
        try:

            w_data = urlopen(self.request)
            raw_data = w_data.read()
            # print(raw_data)

        except URLError:
            raise IndexError("No internet connection available to transfer audio data")
        except:
            raise KeyError("Server wouldn't respond (invalid key or quota has been maxed out)")

        # print('this is wave_gata:',raw_data)
        print("Get the wave data is success ,the length is {}, then play the data……".format(len(raw_data)))
        # self.play_mp3(raw_data)
        return raw_data

    def play_mp3(self,mp3_data):
        import platform,os,stat,time
        import subprocess
        # determine which player executable to use
        system = platform.system()
        # print(system,platform.machine())
        # directory of the current module file, where all the FLAC bundled binaries are stored
        path = os.path.dirname(os.path.abspath(__file__))
        # print(path)

        process = subprocess.Popen("mpg123 -q -" ,
                                   stdin=subprocess.PIPE,
                                   stdout=subprocess.PIPE,
                                   shell=True)
        time.sleep(0.1)
        play_info, stderr = process.communicate(mp3_data)
        return play_info

class TuringChatMode(object):
    """this mode base on turing robot"""

    def __init__(self):

        self.turing_url = 'http://www.tuling123.com/openapi/api?'

    def get_turing_text(self,text):

        turing_url_data = dict(
            key = '21813a76b34546eeb9b487d12cca9a9d',
            info = text,
            userid = 'jack_pi',

        )

        self.request = Request(self.turing_url + urlencode(turing_url_data))
        #print(self.request)

        try:
            w_data = urlopen(self.request)
            #print("this w_data:",w_data)
        except URLError:
            raise IndexError("No internet connection available to transfer audio data")

        except:
            raise KeyError("Server wouldn't respond (invalid key or quota has been maxed out)")

        response_text = w_data.read().decode('utf-8')
        json_result = json.loads(response_text)

        print(json_result)
        return json_result['text']


if __name__ == "__main__":

    tts = TextToSpeech()
    text_data = "浮生万千，挚爱有三，喷薄朝阳，皓婉皎月，不及如你，沧海桑田"
    tts_data =tts.get_wave_data(text_data)

    fs = open("three.wav",'wb')
    fs.write(tts_data)
    fs.close()
