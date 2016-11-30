import RPi.GPIO as GPIO
import array
import json
import time

def init_BTN_pins(buttons, rndbutton):

    GPIO.setup(rndbutton, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    
    for i in buttons:
        GPIO.setup(i, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def checkButtons(buttonArray, buttonStateArray, ledArrary):

    index = 0
    for index, obj in enumerate(buttonArray, start=0):
        if (GPIO.input(buttonArray[index]) == False):
            buttonStateArray[index] = True
        else:
            buttonStateArray[index] = False
            
        index+=1

    return buttonStateArray

def checkRndButton(state, button, buttonStateArray):

    if (GPIO.input(button) == False and not True in buttonStateArray):        
        #bounce compensation
        time.sleep(0.1)
        
        if state == False:
            print "START : RANDOMLY TURNING ON LEDS"
            return True
        else:
            print "STOP : RANDOMLY TURNING ON LEDS"
            return False
    elif True in buttonStateArray:
        return False
    
    return state
