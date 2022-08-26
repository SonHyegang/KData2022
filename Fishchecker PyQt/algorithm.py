from utils.video2img import video2img
from utils.info import *
from utils.rotationimg import *
from PIL import Image 
import numpy as np
import os
import cv2
import re
from detect_1 import *
from detect_2 import *
from detect_3 import *


def run():
    print("Run...")

    filename = 'test'
    video2img(file=filename)

    detect_1()
    print("\nDetect_1 complete!\n")
    # Frame choice(가장 넓은 면적)
    f = open('xyxy.txt')
    lines = f.readlines()
    _lines = []
    
    for l in lines[::-1]:
      #print(l.split('/'))
      if re.match('frame', l.split('/')[0]):
        _lines.append(l.split('/'))
    
    _lines.sort(key=lambda x:int(x[2]), reverse=True)
    bestframe = _lines[0][0]
    bestframepath = '/inference/images'+'/%s'%bestframe
    print("bestframe: ", bestframe)
    print("bestframepath: ", bestframepath)

    print("Detected species")
    species = list(np.array(_lines).T[1])
    species = max(species, key=species.count)
    print()
    print(speciesinfo[species][0])

    # Choice한 frame rotation
    best_img = Image.open(os.path.abspath(__file__) + bestframepath)
    print(os.path.abspath(__file__) + bestframepath)
    print(best_img)
    [best_img.rotate(i).save('./rotatedimg/rotate'+str(i)+'.jpg','jpg') for i in range(0,91,5)]
    [best_img.rotate(i).save('./rotatedimg/rotate'+str(i)+'.jpg','jpg') for i in range(-1,-91,-5)]
    

    detect_2()
    print("\nDetect_2 complete\n")
    f = open('xyxy.txt')
    lines = f.readlines()
    _lines = []
    for l in lines[::-1]:
      #print(l.split('/'))
      if re.match('rotate', l.split('/')[0]):
        _lines.append(l.split('/'))

    _lines.sort(key=lambda x:int(x[4]), reverse = False)
    rotatedbestframe = _lines[0]
    rotatedbestframepath = 'rotatedimg/%s'%rotatedbestframe[0]
    fishIL = int(rotatedbestframe[3])
    print("fishIL: ",fishIL)
    
    for _ in _lines:
      _img = cv2.imread('./rotatedimg/'+_[0], cv2.IMREAD_UNCHANGED)
      #cv2_imshow(_img)
      bgrLower = np.array([10, 0, 10])    # 추출할 색의 하한(BGR)
      bgrUpper = np.array([180, 100, 100])    # 추출할 색의 상한(BGR)
      img_mask = cv2.inRange(_img, bgrLower, bgrUpper) # BGR로 부터 마스크를 작성
      result = cv2.bitwise_and(_img, _img, mask=img_mask) # 원본 이미지와 마스크를 합성
      cv2.imwrite('./bongimg/bongimg'+_[0], result)

    detect_3()
    print("\nDetect_3 complete\n")
    f = open('xyxy.txt')
    lines = f.readlines()
    _lines = []
    for l in lines[::-1]:
      #print(l.split('/'))
      if re.match('bongimg', l.split('/')[0]):
        _lines.append(l.split('/'))

    _lines.sort(key=lambda x:int(x[4]), reverse = False)

    bongIT = int(_lines[0][4])
    fishTL = int(fishIL) * 2.1 / bongIT #fishTL : bongIL = 실제 fishTL : 2.1

  
    f = open("xyxy.txt", 'w')
    f.close()
    
    return species, speciesinfo[species], fishTL, fishIL, bongIT

