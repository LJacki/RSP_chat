#! /usr/bin/python3.4
# _*_coding:utf-8_*_

def play_mp3(mp3_data):
    import platform,os,stat,time
    import subprocess
   
    system = platform.system()
    print(system,platform.machine())
    path = os.path.dirname(os.path.abspath(__file__))
    print(path)
    
    try:
        process = subprocess.Popen("mpg123 -q -",
                                   stdin=subprocess.PIPE,
                                   stdout=subprocess.PIPE,
                                   shell=True)
    except OSError:
        pass
    time.sleep(0.1)
    play_info,stderr = process.communicate(mp3_data)
    return play_info

f = open("chengdu.mp3",'rb')
raw_data = f.read()
f.close()
# print(raw_data)
play_mp3(raw_data)






