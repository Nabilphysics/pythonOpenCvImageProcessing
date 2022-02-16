# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 05:10:03 2022

@author: User
"""

import cv2 
   
# path 
#path = r'C:\Users\Rajnish\Desktop\geeksforgeeks\geeks.png'
   
# Reading an image in default mode
image = cv2.imread('pmhd2.png')
   
# Window name in which image is displayed
window_name = 'Image'
  
# Start coordinate, here (5, 5)
# represents the top left corner of rectangle
start_point = (546, 503)
  
# Ending coordinate, here (220, 220)
# represents the bottom right corner of rectangle
end_point = (643, 538)
  
# Blue color in BGR
color = (255, 0, 0)
  
# Line thickness of 2 px
thickness = 2
  
# Using cv2.rectangle() method
# Draw a rectangle with blue line borders of thickness of 2 px
image = cv2.rectangle(image, start_point, end_point, color, thickness)

#Put Text in a Image
# Using cv2.putText() method
org = start_point
font = cv2.FONT_HERSHEY_SIMPLEX
color = (0, 0, 255)
thinckness = 2
fontScale = 0.7
image = cv2.putText(image, 'OpenCV', org, font, 
                   fontScale, color, thickness, cv2.LINE_AA)  
# Displaying the image 
cv2.imshow(window_name, image) 

# Press Q on keyboard to  exit
cv2.waitKey(0)
cv2.destroyAllWindows()
  
    
  