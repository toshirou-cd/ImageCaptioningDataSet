import time
from datetime import datetime
from numpy import random
file = open('Data/H.A/unNameToken.txt','r')
lines = file.readlines()
print(len(lines))

# import os
# path = 'Data/H.A/unnamedImg'
# files = os.listdir(path)

for indx,line in enumerate(lines) :
    line = line[:line.rfind('#')]
    ms = str(random.randint(1000,99999999))
    strings = time.strftime("%Y%m%d%H")[2:]
    newImgName = strings + ms[:4] + '_89.jpg'
    if(indx % 5 ==0) :
        print(line +"-" +newImgName )
    # for file in files :
    #     os.rename(os.path.join(path, file), os.path.join(path, ''.join([str(index), '.jpg'])))