# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 04:22:56 2022

@author: User
"""

# let's start with the Imports 
import cv2
import easyocr

reader = easyocr.Reader(['en'], gpu = False) 
# Read the image using imread function
image = cv2.imread('pmhd1.png')
cv2.imshow('Original Image', image)
h,w,c = image.shape

print("Original Height ,Width and Channel:", h,"x", w, c)

#gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#a,b = gray.shape
#print("gray Height ,Width and Channel:", a,"x", b)

# Set rows and columns 
# lets downsize the image using new  width and height
down_width = 300
down_height = 200
down_points = (down_width, down_height)
#resize_down = cv2.resize(image, down_points, interpolation= cv2.INTER_LINEAR)
#cv2.imshow('resize', resize_down)

#Resizing With a Scaling Factor
#https://learnopencv.com/image-resizing-with-opencv/
# Scaling Up the image 1.2 times by specifying both scaling factors
scale_up_x = 2.5
scale_up_y = 2.5
# Scaling Down the image 0.6 times specifying a single scale factor.
scale_down = 0.4

#scaled_f_down = cv2.resize(image, None, fx= scale_down, fy= scale_down, interpolation= cv2.INTER_LINEAR)
#scaled_f_up = cv2.resize(image, None, fx= scale_up_x, fy= scale_up_y, interpolation= cv2.INTER_LINEAR)
#cv2.imshow('scaled_f_down', scaled_f_down)

# Cropping an image
#Mid Monitor Image Size
#cropped_image = image[277:287,583:609] #image[y_start:y_end,x_coordinate_start:x_coordinate_end]

#high Monitor Image Size
cropped_image = image[415:432,873:917] #image[y_start:y_end,x_coordinate_start:x_coordinate_end]

# Display cropped image
cv2.imshow("cropped", cropped_image)

gray = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray", gray)



scaled_f_up = cv2.resize(cropped_image , None, fx= scale_up_x, fy= scale_up_y, interpolation= cv2.INTER_LINEAR)
cv2.imshow("Scaled Up", scaled_f_up)

#gray = cv2.cvtColor(scaled_f_up, cv2.COLOR_BGR2GRAY)
#cv2.imshow("gray", gray)

#(thresh, im_bw) = cv2.threshold(scaled_f_up, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
thresh = 65
im_bw = cv2.threshold(gray, thresh, 255, cv2.THRESH_BINARY)[1]
cv2.imshow("binary", im_bw)

result = reader.readtext(im_bw)
print("binary: ",result)

result = reader.readtext(scaled_f_up)
print("Scaled Up",result)

result = reader.readtext(cropped_image)
print("Croped Image:",result)

cv2.waitKey(0)
cv2.destroyAllWindows()