import RPi.GPIO as GPIO
import numpy as np
import array
import time
import json

import LED_GPIO as led 
import BUTTON_GPIO as btn
import parseJson as gjs

rndBtnState = False
interval = .1

rndbtn = gjs.getJsonRnd()

gpioValues = gjs.getJsonData()

strArray = gpioValues[0]
btnArray = gpioValues[1]
ledArray = gpioValues[2]
clrArray = gpioValues[3]

arraySize = len(btnArray)
frequencyArray = [0.0] * arraySize
btnStateArray = [False] * arraySize

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(True)

led.init_LED_pins(ledArray, clrArray)
btn.init_BTN_pins(btnArray, rndbtn)

try:
    while True:

        time.sleep(interval)
        
        btnStateArray = btn.checkButtons(btnArray, btnStateArray, ledArray)
        rndBtnState   = btn.checkRndButton(rndBtnState, rndbtn, btnStateArray)

        if(rndBtnState):
            frequencyArray = led.randomLights(ledArray, frequencyArray)
            led.rnd_RGB_ON(clrArray)
        else:
            led.rnd_RGB_OFF(clrArray)
            led.setLEDs(strArray, btnStateArray, ledArray)

        led.getfrequency(btnStateArray, frequencyArray)

except KeyboardInterrupt:

    print "\n"
    print '%-7s  %-7s  %-10s' % ('color','occurrences','percent')
    print '--------------------------------------------'
    #testing just how random python's random module is
    index = 0
    total = sum(frequencyArray)

#    print tabulate([strArray, frequencyArray], 'color', ' occurrences')
    for index, occurrences in enumerate(frequencyArray):
        s = strArray[index]
        print '%-7s %12d  %-0.2f' % (strArray[index], occurrences, occurrences/total * 100), "%"
        index+=1
    print "\n"
    print "Total : ", total


finally:   
    GPIO.cleanup()
