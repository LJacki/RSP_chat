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

## At Last

Talk is cheap,show me the code.