'''
V 1.0.0
Syed Razwanul Haque (Nabil)

easyocr version 1.4.1
python version 3.8.8
opencv-python version 4.5.3.56
'''


#import os
import easyocr
#from matplotlib import pyplot as plt
#import numpy as np
import cv2
#import time
reader = easyocr.Reader(['en'], gpu = False) 
#en = english model


#cap = cv2.VideoCapture('http://takemotopiano.aa1.netvolante.jp:8190/nphMotionJpeg?Resolution=640x480&Quality=Standard&Framerate=30')
#video file has to be in the same folder
#cap.set( cv2.CAP_PROP_FPS, 1 )
#cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
while True:
    cap = cv2.VideoCapture('http://tamperehacklab.tunk.org:38001/nphMotionJpeg?Resolution=640x480&Quality=Clarity')
    ret, frame = cap.read()
    
    if ret == False:
        print('No Video')
        break
    cv2.imshow('frame', frame)
   
    result = reader.readtext(frame)
    #print(result)
    
    '''
    print("********************************")
    print("\n OCR Result")
    print("\n","Data Length:",len(result))
    
    print("VSM Data:")
    print("Heart Rate: ",result[2][-2])
    print("Pulse: ",result[3][-2])
    print("SpO2: ",result[6][-2])
    
    print("ABP Sys: ",result[8][-2],result[9][-2])
    print("PAP Dia: ",result[11][-2],result[12][-2])
    '''
    for i in result:
        print(i[1])
    print(result)
    
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()