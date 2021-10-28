file = open("Data/H.A/processToken.txt",'r')
lines = file.readlines()
imgName = []
for indx,line in enumerate(lines) :
    if (indx%5 == 0) :
        img = line[:line.rfind("| 0|")]
        imgName.append(img)
print(imgName)
print(len(imgName))

destinationPath = 'Data/H.A/process img'
sourcePath = 'D:/FPTedu/AI/flickr30k_images'

import os
import shutil
import time
from numpy import random



files = os.listdir(sourcePath)
for f in files :
    for img in imgName :
        if (f.startswith(img)) and (img != '') : 
            ms = str(random.randint(1000,99999999))
            strings = time.strftime("%Y%m%d%m")[2:]
            newImgName = strings + ms[:4] + '_89.jpg'
            shutil.move(sourcePath+"/"+img,destinationPath+"/"+newImgName)
            file = open("Data/H.A/processToken.txt",'r')
            line2 = file.readlines()
            for indx,line in enumerate(line2) :
                if(line.__contains__(img)):
                    line2[indx] = newImgName + line
                    out = open("Data/H.A/processToken.txt",'w')
                    out.writelines(line2)
                    out.close()
            

