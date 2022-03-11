import cv2
import numpy as np

def saveFrames(PathVideo, PathFolder):
    cap = cv2.VideoCapture(PathVideo)
    i = 1
    while True:
        ret, frame = cap.read()
        #Условие завершения
        if ret == False or (cv2.waitKey(1) & 0xFF == ord('q')):
            break

        #Показ фрагментов
        cv2.imshow(f'video frames {PathVideo}', frame)

        #Сохранение кадры в папку framse
        #cv2.imwrite(f'{PathFolder}/frame{i}.jpg', frame)
        i += 1;
    cap.release()
    cv2.destroyAllWindows()


saveFrames("vag14_20.mp4","frames")


#img = cv2.imread('kananaskis-alberta-kanada-2900.jpg', cv2.IMREAD_GRAYSCALE)
#cv2.imshow('girl', img)
#cv2.waitKey(0)
#i = 5;
#cv2.imwrite(f'frames/frame{i}.jpg', img) #"C:\Users\Public\Desktop\PyCharm Community Edition 2021.3.2.lnk"