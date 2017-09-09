#! usr/bin/python3.4
# _*_coding:utf-8_*_

import RPi.GPIO as GPIO
import time

PIN_red = 11
PIN_green = 13
PIN_blue = 15

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN_red,GPIO.OUT)
GPIO.setup(PIN_green,GPIO.OUT)
GPIO.setup(PIN_blue,GPIO.OUT)

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

        
      
