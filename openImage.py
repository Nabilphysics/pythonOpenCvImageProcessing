# -*- coding: utf-8 -*-
"""
https://www.geeksforgeeks.org/python-opencv-cv2-puttext-method/
#https://www.tutorialkart.com/opencv/python/opencv-python-resize-image/
"""

import cv2

#read image
img = cv2.imread('a.jpg')

# get dimensions of image
dimensions = img.shape

# height, width, number of channels in image
height = img.shape[0]
width = img.shape[1]
channels = img.shape[2]

print('Image Dimension    : ',dimensions)
print('Image Height       : ',height)
print('Image Width        : ',width)
print('Number of Channels : ',channels)

img_resize = cv2.resize(img, (648,368)) #https://www.tutorialkart.com/opencv/python/opencv-python-resize-image/
cv2.imshow('sample image',img_resize)

# read image as grey scale
grey_img = cv2.imread('a.jpg', cv2.IMREAD_GRAYSCALE)
grey_img_resize = cv2.resize(grey_img, (648,368)) 
cv2.imshow('Grey Scale',grey_img_resize) 

edges = cv2.Canny(grey_img_resize,50,200)
cv2.imshow("Edge Detected Image", edges)

# Using cv2.cvtColor() method
# Using cv2.COLOR_BGR2HSV color space
# conversion code
hsv_color_space = cv2.cvtColor(img_resize, cv2.COLOR_BGR2HSV)
cv2.imshow('HSV Color Space', hsv_color_space)

cv2.waitKey(0) # waits until a key is pressed
cv2.destroyAllWindows() # destroys the window showing image