import RPi.GPIO as GPIO
import numpy as np
import array
import json
from random import randint

def init_LED_pins(leds, clr):

    for color in clr:
        GPIO.setup(color['red'], GPIO.OUT)
        GPIO.setup(color['blue'], GPIO.OUT)
        GPIO.setup(color['green'], GPIO.OUT)
        
    for led in leds:
        GPIO.setup(led, GPIO.OUT)

def setLEDs(strArray, buttonStateArray, ledArray):

    index = 0
    for index, obj in enumerate(buttonStateArray, start=0):        
        if obj == True:
            GPIO.output(ledArray[index], GPIO.HIGH)
            print strArray[index] + " has been pushed"

        else:
            GPIO.output(ledArray[index], GPIO.LOW)
        index+=1

def randomLights(ledArray, freqArray):

    lsize = len(ledArray)
    bitArray = [None] * lsize
    for index, led in enumerate(ledArray, start=0):
        n = randint(0,1)
        
        if n == 1:            
            GPIO.output(led, GPIO.HIGH)
            bitArray[index] = True
        else:
            GPIO.output(led, GPIO.LOW)
            bitArray[index] = False

    return getfrequency(bitArray, freqArray)
   
def getfrequency(bitArray, freqArray):

    for index, i in enumerate(bitArray, start=0):
        if i == True:
            freqArray[index]+=1

    return freqArray
        
def STOPALL_LEDs(ledArray):
    for led in ledArray:
        GPIO.output(led, GPIO.LOW)

def rnd_RGB_ON(rgbArray):
     for rgb in rgbArray:
        z = {rgb['red'], rgb['blue'], rgb['green']}

        for i in z:
            n = randint(0,1)

            if n == 1:
                GPIO.output(i, GPIO.HIGH)
            else:
                GPIO.output(i, GPIO.LOW)

def rnd_RGB_OFF(rgbArray):
     for rgb in rgbArray:
         z = {rgb['red'], rgb['blue'], rgb['green']}
         
         for i in z:
             GPIO.output(i, GPIO.LOW)
