import cv2
import os

def video2img(videoPath = './python/classifiers/yolov7/testdata/', file = 'video'):
    """
    Video Sampling
    Path : Fishchecker/example
    """
    path1 = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))
    path2 = os.path.abspath(os.path.join(path1, '..'))
    print(path1, path2)

    imagePath = './python/classifiers/yolov7/testdata/images/'
    #file_list = os.listdir(videoPath)
    
    if not (os.path.isdir(videoPath + file)):
        os.makedirs(os.path.join(imagePath + file))

    cap = cv2.VideoCapture(videoPath + file +'.mp4')
    print(videoPath+file +'.mp4')
    count = 0

    while (cap.isOpened()):
        ret, image = cap.read()

        if ret == False:
            break
        if count%5 == 0:
            cv2.imwrite(imagePath + file + "/frame%d.jpg" % count, image)

        #print('%d.jpg done' % count)
        count += 1
    print('Video2Img complete')
    cap.release()
    

    # try:
    #     #if not (os.path.isdir(videoPath + file)):
    #     #    os.makedirs(os.path.join(imagePath + file))

    #     cap = cv2.VideoCapture(videoPath + file)

    #     count = 0

    #     while (cap.isOpened()):
    #         ret, image = cap.read()

    #         if ret == False:
    #             break
    #         if count%5 == 0:
    #             cv2.imwrite(imagePath + file + "/frame%d.jpg" % count, image)

    #         print('%d.jpg done' % count)
    #         count += 1

    #     cap.release()

    # except OSError as e:
    #     print(e)
    #     raise
