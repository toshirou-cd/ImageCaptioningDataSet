file = open("Data/H.A/processToken.txt",'r')
lines = file.readlines()
imgName = []
for indx,line in enumerate(lines) :
    if (indx%5 == 0) :
        img = line[:line.rfind("#0")]
        imgName.append(img)
print(imgName)
print(len(imgName))

destinationPath = 'Data/H.A/process img'
sourcePath = 'D:/FPTedu/AI/flickr30k_images'

import os
import shutil
import time



files = os.listdir(sourcePath)
for f in files :
    for img in imgName :
        if (f.startswith(img)) and (img != '') : 
            
            shutil.move(sourcePath+"/"+img,destinationPath+"/"+img)
            

