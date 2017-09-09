# RSP_chat
U can talk something with the raspberry_pi which named "Orange",also can say some keywords to control other things.

算了，我们还是说中文吧，这样感觉亲切一点。

## 使用平台

硬件环境：树莓派3代B+（Raspberry Pi 3 B+）

软件环境：Linux发行版RaspDebian

语言版本：python3.4

所需python package：os , json , time , base64 , urllib , platform , stat , subprocess 

安装应用：mpg123、omxplayer

文件存放路径：path = "/home/pi/RSP_ chat"

录音设备：CM108IC树莓派亲测免驱动

## 文件结构

工程名为：RSP_chat，里面包含两个文件夹，六个文件，实例如下：

- \_pycache\_ 
- media
- chatStart.sh
- led.py
- led.pyc
- RSP_chat.py
- RSP_chat_ok.py
- samples.wav

其中\_pycache_ 、led.py、led.pyc、是为了用语音控制其他器件，python对应的模块的调用，编译之后生成的一系列文件。

media文件夹内存放的为`windows XP`平台下经典的开关机音频文件，和一些特征比较突出的音频文件，用于程序的开始和结束，以及模式状态转换作为声音提示。

chatStart.sh是设置主程序RSP_chat.py在系统开机后自动运行。

RSP_chat_ok.py为过程测试文件，也可以单独使用。

RSP_chat.py为主程序文件。

## 你需要知道

### 百度语音识别

这一部分可以从百度语音识别官方网站获取，语音识别的API接口方式，有详细的文档参考：[API请求方式及参数基本说明](http://yuyin.baidu.com/docs/asr/57) ,一些传输格式的详细介绍不知道我以后还会不会更新。

### 百度语音合成

话不多说，直接上文档参考：[在线语音合成REST API SDK](http://yuyin.baidu.com/docs/tts/196)，需要说明的是，这个文档在07.06.30号被更新了，包括上面的百度语音识别都有百度给的python的库了，这个工程是在跟新之前做的，大概看了一下，新的库支持比较多种类的语言，而且功能拓展到了人脸识别，自然语言处理，OCR图像识别等。可以直接安装并支持python2.7.+，3.+

### 图灵机器人接入

估计已经猜出来了，没错还是[图灵机器人web API](http://www.tuling123.com/help/h_cent_webapi.jhtml?nav=doc) ，用过之后才知道，这个图灵机器人真是强大到没朋友，后台可以分析数据，可以批量导入问题以及答案，还支持敏感词汇关注。最近也有更新，用过了都说好。

## 还需要知道

上次我看到百度的语音文档编辑的时间还是15年左右，最近又迎来了一批文档更新，相信科大讯飞也能给出API的解决方案，至于免费不免费，另说吧。图灵机器人也在成长，各大平台都想顶在智能家居，机器学习的风口浪尖，我们在借助各种平台的同时，一定要去深究其本质，只学习到怎么使用别人的接口，也始终只是会用，而无法获得知其所以然的快感。

这款工程虽然做出来了，但是显得一点都不智能。

其一，因为在语音接收的问题上，由于树莓派平台的限制，并不能实现连续性的扫描周围的声音，而我在windows 10，pycharm上使用的时候是可以用PyAudio Package来进行实时读取音频信息的，到了树莓派上目前的解决方案是隔一段时间读取一次，为了检测准确还配了个指示灯说明。

其二，显得整个机器人很傻，一直在从网上获取信息，显得反应很迟钝，而且要达到真正的智能还有很长路要走，这一方面，百度语音合成跟新之后应该在合成速度上有些改善，但我们还需要多多思考，步步优化。

## 对象介绍

为了方便了解，还是做一下简单的介绍，有利于对整个模块工作方式的了解。

### class GetToken(object)

词法分析是计算机科学中将字符序列转换为标记（token）序列的过程，从输入字符流中生成标记的过程叫作标记化（tokenization），在这个过程中，词法分析器还会对标记进行分类。此对象用来获取连接网络的`token`，通过标识

```python
API_KEY ="76723YF5OUIkBgW9iyDb9DPW"，
API_SECRET= "392c0282fd778dbd3d75051673ffa19b"
```

为百度语音平台的密钥，转换成网络标识的标准形式，以UTF-8的编码方式保存，用于每次访问百度语音平台。

### class GetVoiceData(object)

```python
def get_voice(self):

	print("Start recording :")
	os.system('arecord -D "plughw:1,0" -f S16_LE -d 5 -r16000 {}'.format(self.filename))
    print("Done!")
	wf = open(self.filename,"rb")
	voice_data = wf.read()
	wf.close
	return voice_data
```

此对象通过函数get_voice()调用操作系统指令，用命令行的形式以每5秒钟截取一次周围音频信号，并以16000Khz的采样频率进行采样，将音频数据保存为文件`samples.wav`，并返回`voice_data`为音频二进制数据。

### class SoundToText(object)

```python
	def __init__(self, language = "zh"):
	def get_text_data(self,voice_data): 
```

此对象主要功能为以固定参数形式将音频数据传入百度语音识别API接口。语言为中文，采样频率为16000Khz，标识为本机MAC地址，上传音频格式为WAV，其中上传音频内容需要进行`base64`编码。以`JSON格式`向网站发送GET请求，尝试打开接入url，如果出现异常会出现异常退出并提示：`IndexError`或者`KeyError`。

如果接入顺利，网站返回json_result[]，其中`json_result[‘result’]`为语音识别结果，方法`get_text_data(self,data)`，以音频二进制数据为形参，返回语音识别结果以UTF-8解码存储在二维组元json_result[‘result’]\[0]。

### class TuringChatMode(object)

```python
	def __init__(self):
    def get_turing_text(self,text):
```

此对象实现的功能为接入Turing机器人，以从百度语音识别的文本数据为形参，传入方法`get_turing_text(self,text)`（获取方式与上述中访问百度语音API方法类似，此处不再累述），函数返回从Turing机器人对话后返回的文本数据。

### class TextToSpeech(object)

```python
	def __init__(self,language = "zh"):
	def get_wave_data(self,text):
	def play_mp3(self,mp3_data):
```

此对象实现的功能为接入百度语音合成API（获取方式与上述中访问百度语音API方法类似，此处不再累述），以Turing机器人返回文本数据为形参传入`get_wave_data(self,text)`方法，获取从百度语音返回的对应文本的音频数据。文本数据以流媒体播放模式通过`play_mp3(self,mp3_data)`方法播出。

## \_\_main\_\_介绍

程序开始将给不同功能的对象命名：

```python
if __name__ == "__main__":
    rec = GetVoiceData()
    stt = SoundToText()
    turing = TuringChatMode()
    tts = TextToSpeech()
```

进入程序启动问候：

```python
tts.get_wav_data("xp.wav")
time.sleep(2)
greet_data = "您好，欢迎您使用小橘子语音！"
tts.get_wave_data(greet_data)
```

之后就一直进行函数主题循环，通过一些标志位如`exitChatFlag`等来作为改变对话或者控制状态的标致，配合严谨的逻辑规律，分别说出“嗨！小橘子”进入语音聊天模式，进入此模式后就可以跟小橘子聊天了，聊天内容涉及天气，航班，笑话，成语，时间，歇后语等常用词库，语音输入“聊天结束”来结束聊天。

此外，可以通过语音输入“结束程序”，“关灯”，“播放一首歌”，“关机”等来实现相应功能。当程序运行时，如果没有检测到周围环境的语音消息，会主动提示一些常用的关键词：

```python
tts_data="你可以这样说：‘嗨小橘子’，‘聊天结束’，‘播放一首歌’，‘结束程序’，‘关机’等等"
	tts.get_wave_data(tts_data)
```

通过这样提示，帮助使用者更容易亲近小橘子，这种方式是一种语音式的使用说明书。

当然，在最终成品我已经把这一段弃掉了，因为 太啰嗦了。

程序最后设置成开机启动，这样每次运行系统的时候，可以不用进入图形界面，就能自动运行程序。程序初始加入了经典的`Windows XP`开机声音，用于跟用户之间进行交互，后来在程序结束，聊天结束，以及关机等不明显的交互阶段，加入了声音提示，方便用户理解当前程序运行的进程。其中结束程序用于调试时强行终止程序。

## At Last

Talk is cheap,show me the code.