import cv2
import os

def video2img(videoPath = '/inference/', file = 'test'):
    """
    Video Sampling
    Path : Fishchecker/inference
    """
    path1 = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))
    path2 = os.path.abspath(os.path.join(path1, '..'))
    print(path1, path2)

    imagePath = '/inference/images'
    file_list = os.listdir(videoPath)
    
    if not (os.path.isdir(path2 + imagePath)):
        os.makedirs(os.path.join(path2 + imagePath))

    cap = cv2.VideoCapture(path2 + videoPath + file +'.mp4')
    print(path2 + videoPath+file +'.mp4')
    count = 0

    while (cap.isOpened()):
        ret, image = cap.read()

        if ret == False:
            break
        if count%5 == 0:
            cv2.imwrite(path2 + imagePath + "/frame%d.jpg" % count, image)
            print(path2 + imagePath+"/frame%d.jpg" % count)
            # print('%d.jpg done' % count)
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
