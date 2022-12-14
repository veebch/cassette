#!/usr/bin/python3
# -*- coding:UTF-8 -*-
# Code at github.com/llvllch/cassette 
# Aug' 22

#--------------Driver Library-----------------#
import RPi.GPIO as GPIO
import OLED_Driver as OLED
#--------------Image Library---------------#
from PIL  import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageColor
#--------------Data Grabber and other---------------#
import urllib, json
import requests
import random
import os
import glob
import time
import yaml
#-------------Display Functions---------------#

dirname = os.path.dirname(__file__)
picdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'images')
fontdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts')
configfile = os.path.join(os.path.dirname(os.path.realpath(__file__)),'config.yaml')

with open(configfile) as f:
    config = yaml.load(f, Loader=yaml.FullLoader)
api=config['api']
id=config['id']

def Display_Picture(File_Name,score):
    image = Image.open(File_Name)
    draw = ImageDraw.Draw(image)
    if score>0:
        prettynum = format(score,",")
    else:
        prettynum = ""
    font = ImageFont.truetype(os.path.join(fontdir,'RobotoCondensed-Bold.ttf'),22)
    draw.text((35, 103), prettynum, fill = "BLACK", font = font)
    angle = 90
    image = image.rotate(angle, expand=True)
    OLED.Display_Image(image)


def getindex(api,id):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    url="https://www.googleapis.com/youtube/v3/channels?part=statistics&id="+id+"&key="+api
    try:
        youtubestats=requests.get(url, headers=headers).json()
        data= youtubestats['items']
        score=data[0]['statistics']['subscriberCount']
    except:
        score=0
    return score
    
#----------------------MAIN-------------------------#
try:

    def main():
    
        #-------------OLED Init------------#
        OLED.Device_Init()
        Display_Picture(os.path.join(picdir, "heart.jpg"),0)
        OLED.Delay(2000)
        Display_Picture(os.path.join(picdir, "heartend.jpg"),0)
        OLED.Delay(2000)
        Display_Picture(os.path.join(picdir, "heart.jpg"),0)
        OLED.Delay(2000)
        while True:
            score=getindex(api,id)
            print(score)
            Display_Picture(os.path.join(picdir, "heartYT.jpg"),score)
            time.sleep(120)
    if __name__ == '__main__':
        main()

except:
    print("\r\nInterrupted, End")
    OLED.Clear_Screen()
    GPIO.cleanup()
