import os
import easyocr
from matplotlib import pyplot as plt
import numpy as np
import cv2

reader = easyocr.Reader(['en'], gpu = False)

cap = cv2.VideoCapture('http://takemotopiano.aa1.netvolante.jp:8190/nphMotionJpeg?Resolution=640x480&Quality=Standard&Framerate=30')
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

while True:
    ret, frame = cap.read()

    cv2.imshow('frame', frame)
    result = reader.readtext(frame)
    print(result)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()