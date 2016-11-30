import json
import numpy as np
import array

def getJsonRnd():
    with open('GPIO_values.json') as data_file:
        conf = json.load(data_file)
        btn = conf['randomButton']
        
        return btn
    
def getJsonData():

    with open('GPIO_values.json') as data_file:
        conf = json.load(data_file)
        
        mainStuff = conf['InputOutput']['mainStuff']
        colorLED = conf['InputOutput']['colorLED']
        
        StrArray = ["0"] * len(mainStuff)
        BtnArray = [0] * len(mainStuff)
        LedArray = [0] * len(mainStuff)
        ClrArray = [0] * len(colorLED)

        cIndx = 0
        for cIndx, obj in enumerate(colorLED, start = 0):
            ClrArray[cIndx] = obj
            cIndx+=1

        mIndx = 0
        
        for mIndx, obj in enumerate(mainStuff, start=0):
            StrArray[mIndx] = obj['color']
            BtnArray[mIndx] = obj['button']
            LedArray[mIndx] = obj['led']
            
            mIndx+=1

        #return array with 3 1d arrays
        sblArray = np.array([StrArray, BtnArray, LedArray, ClrArray])

        return sblArray
