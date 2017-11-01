# Python实现图灵机器人交互

---

## Where r u from

这篇博文节选自本人在`Github` 的项目[RSP_chat](https://github.com/LJacki/RSP_chat) ，其功能是通过百度语音识别，图灵机器人及百度语音合成功能，实现基于树莓派(Raspberry Pi)的语音交互。在此，截取其中的接入中文语境下的最强大脑——turingRobot API，实现可以打字聊天的衍生Robot。

---

## About TuringRobot

### Introduction

图灵机器人API是在人工智能的核心能力（包括语义理解、智能问答、场景交互、知识管理等）的基础上，为广大开发者、合作伙伴和企业提供的一系列基于云计算和大数据平台的在线服务和开发接口。

### Function

智能对话、知识库、技能服务是图灵机器人三大核心功能。智能对话是指，图灵机器人可赋予软硬件产品中文自然语言交互的能力；知识库是指图灵机器人用户可为机器人导入独家内容以满足个性化及商业化需要；技能服务是指，图灵机器人打包提供超500种实用生活服务技能，涵盖生活、出行、学习、金融、购物等多个领域，一站式满足用户需求。

### How to Use

TuringRobot 官方给出了详细的[Web API-帮助中心 ](http://www.tuling123.com/help/h_cent_webapi.jhtml?nav=doc) ，使用流程中包含注册账号，获取APIKEY，请求方式等详细信息，最初开发者在使用的时候不妨详细阅读此卡发文档。

---

## Show Me the Code

### Platform

初期在`Raspberry Pi 3` 上进行开发的，在`Terminal` 中直接运行_turingRobot.py_ 就能运行。

后期在`windows 7` 下用`Python 3.6`  做了简单的修改，所以直接在`CMD中` 运行或在`Pycharm` 中直接运行_turingRobot.py_ 也没有问题。

### Complete Code

```python
#! /usr/bin/python3.4
# _*_ encode:utf-8_*_

import json

from urllib.request import urlopen,Request
from urllib.error import URLError
from urllib.parse import urlencode

class TuringChatMode(object):
    """this mode base on turing robot"""

    def __init__(self):
        # API接口地址
        self.turing_url = 'http://www.tuling123.com/openapi/api?'

    def get_turing_text(self,text):
        ''' 请求方式:   HTTP POST
            请求参数:   参数      是否必须        长度          说明
                        key        必须          32           APIkey
                        info       必须          1-32         请求内容，编码方式为"utf-8"
                        userid     必须          32           MAC地址或ID
        '''
        turing_url_data = dict(
            key = '21813a76b34546eeb9b487d12cca9a9d',
            info = text,
            userid = 'MAC_ID',

        )
        # print("The things to Request is:",self.turing_url + urlencode(turing_url_data))
        self.request = Request(self.turing_url + urlencode(turing_url_data))
        # print("The result of Request is:",self.request)

        try:
            w_data = urlopen(self.request)
            # print("Type of the data from urlopen:",type(w_data))
            # print("The data from urlopen is:",w_data)
        except URLError:
            raise IndexError("No internet connection available to transfer txt data")
            # 如果发生网络错误，断言提示没有可用的网络连接来传输文本信息
        except:
            raise KeyError("Server wouldn't respond (invalid key or quota has been maxed out)")
            # 其他情况断言提示服务相应次数已经达到上限

        response_text = w_data.read().decode('utf-8')
        # print("Type of the response_text :",type(response_text))
        # print("response_text :",response_text)

        json_result = json.loads(response_text)
        # print("Type of the json_result :",type(json_result))
        return json_result['text']

if __name__ == '__main__':
    print("Now u can type in something & input q to quit")

    turing = TuringChatMode()

    while True:
        msg = input("\nMaster:")
        if msg == 'q':
            exit("u r quit the chat !")			# 设定输入q，退出聊天。
        else:
            turing_data = turing.get_turing_text(msg)
            print("Robot:",turing_data)

```

所有`print` 注释均为调试时候用，正常跑代码时注释掉。

### How to Use

无论在**树莓派终端** ，还是**CMD** 中的使用都是直接运行代码文件_turingRobot.py_ ，这里提供一种在`windows` 下比较方便的使用方法，免去平时每次使用都是进入**CMD** 的麻烦。

1. 桌面建立文件：turingRobot.bat

2. 右键以你常用的编辑器（Atom，sbulime，notepad++，Ultra Edit and so on）或者直接用文本打开，进行如下编辑：

   ```bash
   @echo off
   python F:\Python_Code\turingRobot\turingRobot.py
   # 此路径为存放code的路径，python需要添加环境变量
   pause
   ```

3. 保存并退出。

4. 双击运行出现如下对话框：

   ![example01](F:\Python_Code\turingRobot\example01.png)

   此时便进入了对话界面，如果有兴趣，还可以对`CMD` 的界面进行控制，如果没兴趣，可以直接对话，如果写入英文，则直接翻译成中文，所以当一个翻译字典来说是相当便捷的。

   ```bash
   Now u can type in something & input q to quit

   Master:what can i do for u
   Robot: 我能为你做什么

   Master:wednesday
   Robot: 周三
   ```

   如果直接询问中文，也是杠杠的，具体回答需要你丰富自己机器人的库，或者添加已有库的功能。

   ```bash
   Master:今天天气怎么样
   Robot: 请问你想查询哪个城市

   Master:上海
   Robot: 上海:周三 11月1日,晴 东南风,最低气温14度，最高气温22度
   ```

   天气这中东西还支持上下文理解，但是如果在复杂一点的话，就可能收到限制。讲笑话，歇后语加计算这种东西随便试。

   ```bash
   Master:讲一个笑话
   Robot: 昨天郭天王大婚，方爸爸说，女婿我是听你的歌长大，你是我的偶像。从小到大就喜欢你唱的歌，现在我把女儿许配给你，你以后要好好照顾她，照顾她照顾她！！！

   Master:歇后语
   Robot: 口渴碰到清泉水――正合适

   Master:56*989+2562-656
   Robot: 56*989+2562-656=57290
   ```

   具体功能建议到自己机器人网页里进行配置。

开始肆无忌惮的聊天吧，聊一段时间你就能感觉到这机器人不是很智能。可以给自己的机器人设定角色，比如名字，星座年龄，父母等一些特定的设置。一些比较普遍的问题回答的比较块，也可以针对私人的问题在对应的机器人知识库里面添加，图灵机器人官方是支持批量导入知识库的。关于上下文的认知上，有时候可以很好的衔接，但是有些上下文不能很好的连接在一起。

---

## Defect

官网的数据查看比较详细，最近有版本更新，可以查看最近的聊天记录，可以针对回答不好的记录做修改。使用多次后，体验到了一些缺陷，先mark：

- 从英文转中文，直接打英文，就能翻译，但是从中文转英文，需要加’‘的单词是什么’‘。
- 有时候莫名其妙重复一句话。
- 因为在线的API接入，受网络接入延迟影响较大。
- 如果多次说一句话，就不能很好的对应了。

总的来说，这个机器人的接入还是蛮简单的，有趣的。

---

## After

从这里面深刻体会到了，不能像跟人一样交流，来跟机器交流，或者说，与机器交流的方式与跟人类交流的方式，差距还是很大的，希望机器发展的更加`enmotional` 。

最后，Enjoy It！
