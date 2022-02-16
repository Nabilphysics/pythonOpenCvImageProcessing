# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 05:44:27 2022

@author: User
"""

# Python program to explain cv2.rectangle() method 
   
# importing cv2 
import cv2 
   
# path 

   
# Reading an image in default mode
image = cv2.imread('nabil.jpg')
   
# Window name in which image is displayed
window_name = 'Image'
  
# Start coordinate, here (5, 5)
# represents the top left corner of rectangle
start_point = (0, 0)
  
# Ending coordinate, here (220, 220)
# represents the bottom right corner of rectangle
end_point = (300, 550)
  
# Blue color in BGR
color = (255, 0, 0)
  
# Line thickness of 2 px
thickness = 2
  
# Using cv2.rectangle() method
# Draw a rectangle with blue line borders of thickness of 2 px
image = cv2.rectangle(image, start_point, end_point, color, thickness)
  
# Displaying the image 
cv2.imshow(window_name, image) 
cv2.waitKey(0)
cv2.destroyAllWindows()