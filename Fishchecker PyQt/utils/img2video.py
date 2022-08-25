import cv2
import numpy as np
import glob

def img2video(imgPath = './runs/detect/')
    frameSize = (600, 600)

    out = cv2.VideoWriter('output_video.mp4',cv2.VideoWriter_fourcc(*'DIVX'), 10, frameSize)

    for filename in glob.glob(imgPath + '*.jpg'):
        img = cv2.imread(filename)
        out.write(img)

    out.release()
