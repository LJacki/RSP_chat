#! usr/bin/python3.4
# _*_coding:utf-8_*_

'''
	此文件只是为了便于观察orange处于哪一种状态，
	作为辅助功能使用，接入到语音控制的主模块中
	实现通过语音来控制IO口,
	对于控制部分功能的实现，还未深度拓展。
'''
import RPi.GPIO as GPIO
import time

# 设置三种灯的GPIO输出引脚为 pin11，pin13，pin15
PIN_red = 11
PIN_green = 13
PIN_blue = 15

# 屏蔽引脚输出设置的警告（具体原因，没有深入，
# 如果不写也没问题）
GPIO.setwarnings(False)

# 配置IO口的模式
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN_red,GPIO.OUT)
GPIO.setup(PIN_green,GPIO.OUT)
GPIO.setup(PIN_blue,GPIO.OUT)

# 通过简单的控制IO口高低电平来给让灯亮
def red_on():
    GPIO.output(PIN_red,GPIO.HIGH)

def red_off():
    GPIO.output(PIN_red,GPIO.LOW)

def green_on():
    GPIO.output(PIN_green,GPIO.HIGH)

def green_off():
    GPIO.output(PIN_green,GPIO.LOW)

def blue_on():
    GPIO.output(PIN_blue,GPIO.HIGH)

def blue_off():
    GPIO.output(PIN_blue,GPIO.LOW)

# 以亮灭的时间来控制等亮灭的频率，实现闪烁功能
def red_blink(freq):
    red_on()
    time.sleep(1/freq)
    red_off()
    time.sleep(1/freq)

def green_blink(freq):
    green_on()
    time.sleep(1/freq)
    green_off()
    time.sleep(1/freq)

def blue_blink(freq):
    blue_on()
    time.sleep(1/freq)
    blue_off()
    time.sleep(1/freq)

# 用循环实现长时间的固定频率闪烁
def all_blink(times,freq):
    for i in range(times):
        red_on()
        green_on()
        blue_on()
        time.sleep(1/freq)
        red_off()
        green_off()
        blue_off()
        time.sleep(1/freq)

def run_blink(times,freq):
    for i in range(times):
        red_blink(freq)
        green_blink(freq)
        blue_blink(freq)

def run_fast():
    run_blink(10,30)
    all_blink(10,30)

def run_slow():
    run_blink(3,2)
    all_blink(10,30)

def red_blink_times(times,freq):
    for i in range(times):
        red_blink(freq)
