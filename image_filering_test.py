# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 20:18:32 2022

@author: User
"""

import cv2

import numpy as np
font = cv2.FONT_HERSHEY_SIMPLEX

red_color = (0, 0, 255) #red
# Blue color in BGR
blue_color = (255, 0, 0)
thinckness_box = 2
fontScale = 0.7

#Image Info: Capture webcam 2  480p
#XTL and YTL= x and y coordinate_top_left , XBR and YBR = x and y coordinate of botom left rectangle
tempCor = {"XTL":658, "YTL":334 ,"XBR":695, "YBR":352}  
bpmCor = {"XTL":563, "YTL":40 ,"XBR":698, "YBR":157}  
spo2Cor = {"XTL":572, "YTL":218 ,"XBR":651, "YBR":288} 
prCor = {"XTL":743, "YTL":221 ,"XBR":795, "YBR":263} 
respCor = {"XTL":558, "YTL":310 ,"XBR":609, "YBR":361} 
bloodPressureCor = {"XTL":144, "YTL":406 ,"XBR":356, "YBR":477} 
mmHgCor = {"XTL":407, "YTL":442 ,"XBR":460, "YBR":471} 



frame = cv2.imread('C://Users/User/Desktop/PythonCode/openCvPractice/WebcamPics/WebcamPics/CaptureWebcam2_480p.png') 
cropped_temp = frame[tempCor["YTL"]:tempCor["YBR"],tempCor["XTL"]:tempCor["XBR"]]

cv2.imshow('Frame', cropped_temp)

gray_temp = cv2.cvtColor(cropped_temp, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray_temp', gray_temp)  

(T, threshInv) = cv2.threshold(gray_temp, 0, 255,
	cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    
cv2.imshow("Threshold", threshInv)
print("[INFO] otsu's thresholding value: {}".format(T))
    

scale_up_x = 2.5
scale_up_y = 2.5
scaled_up_temp = cv2.resize(gray_temp , None, fx= scale_up_x, fy= scale_up_y, interpolation= cv2.INTER_LINEAR)
cv2.imshow('scaled_up_temp',scaled_up_temp)

thresh = 180
binary_temp = cv2.threshold(gray_temp, thresh, 255, cv2.THRESH_BINARY)[1]
cv2.imshow("binary_temp", binary_temp)
    
filter = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
    # Applying cv2.filter2D function on our Logo image
sharpen_img_2=cv2.filter2D(scaled_up_temp,-1,filter)
#cv2.imshow('sharpen_img',sharpen_img_2)

    
cv2.waitKey(0)
cv2.destroyAllWindows()