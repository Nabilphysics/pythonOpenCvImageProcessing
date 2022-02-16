# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 01:07:16 2022

@author: User
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 05:44:22 2022

@author: Syed Razwanul Haque (Nabil)
Engineering Lead, Hardware Team, Bioforge Health Systems Ltd
"""

#import vlc
import cv2
import easyocr
import numpy as np
#from datetime import datetime
#from discord_webhook import DiscordWebhook

reader = easyocr.Reader(['en'], gpu = False)   

#import time

#discordWebhookUrl = 'https://discord.com/api/webhooks/938841550077714433/1zRvqe64FNkIcBMtjQ5tPDjZQTI8-XOFAFcXXRGOzeGI4iXwK_6HXyFSCplcytm2OANO'

font = cv2.FONT_HERSHEY_SIMPLEX

red_color = (0, 0, 255) #red
# Blue color in BGR
blue_color = (255, 0, 0)
thinckness_box = 2
fontScale = 0.7

'''
#Coordinate to Crop and draw Rectangle 
#XTL and YTL= x and y coordinate_top_left , XBR and YBR = x and y coordinate of botom left rectangle
tempCor = {"XTL":879, "YTL": 401,"XBR":923, "YBR":421}  
bpmCor = {"XTL":776, "YTL": 113,"XBR":972, "YBR":230}  
spo2Cor = {"XTL":769, "YTL":292 ,"XBR":890, "YBR":355} 
prCor = {"XTL":939, "YTL":279 ,"XBR":1020, "YBR":332} 
respCor = {"XTL":778, "YTL":386 ,"XBR":852, "YBR":435} 
bloodPressureCor = {"XTL":362, "YTL":495 ,"XBR":583, "YBR":565} 
mmHgCor = {"XTL":625, "YTL":523 ,"XBR":700, "YBR":551} 
'''


#Image Info: Capture webcam 2  480p
#XTL and YTL= x and y coordinate_top_left , XBR and YBR = x and y coordinate of botom left rectangle
#tempCor = {"XTL":658, "YTL":334 ,"XBR":695, "YBR":352}  
tempCor = {"XTL":658, "YTL":334 ,"XBR":695, "YBR":352}
bpmCor = {"XTL":563, "YTL":40 ,"XBR":698, "YBR":157}  
spo2Cor = {"XTL":572, "YTL":218 ,"XBR":651, "YBR":288} 
prCor = {"XTL":743, "YTL":221 ,"XBR":795, "YBR":263} 
respCor = {"XTL":558, "YTL":310 ,"XBR":609, "YBR":361} 
bloodPressureCor = {"XTL":144, "YTL":406 ,"XBR":356, "YBR":477} 
mmHgCor = {"XTL":407, "YTL":442 ,"XBR":460, "YBR":471} 

#directory = "C://Users/User/Desktop/PythonCode/openCvPractice/snapshot/snapshot"  
# creating vlc media player object
#media_player = vlc.MediaPlayer()
  
# media object
#media = vlc.Media("http://tamperehacklab.tunk.org:38001/nphMotionJpeg?Resolution=640x480&Quality=Clarity")
#media = vlc.Media("vsmEspCam1.mp4")
  
# setting media to the media player
#media_player.set_media(media)
  
# setting video scale
#media_player.video_set_scale(1)
  
# start playing video
#media_player.play()
  
# wait so the video can be played for 5 seconds
# irrespective for length of video
#time.sleep(5)

#path = directory + 'nabil.png'

while True:  
# taking screen shot
    #start_time = datetime.now()
    #media_player.video_take_snapshot(0,path, 0, 0)
    
    #time.sleep(2)
    #frame = cv2.imread('C://Users/User/Desktop/PythonCode/openCvPractice/snapshot/snapshotnabil.png') 
    frame = cv2.imread('C://Users/User/Desktop/PythonCode/openCvPractice/WebcamPics/WebcamPics/CaptureWebcam2_480p.PNG') 
    
    #cv2.imshow('image', frame) 
  
    # Maintain output window utill
    # user presses a key
    #cv2.waitKey(0)        
  
    # Destroying present windows on screen
    #cv2.destroyAllWindows() 
    
    # Cropping the point of interest to extract data
   
    
    cropped_temp = frame[tempCor["YTL"]:tempCor["YBR"],tempCor["XTL"]:tempCor["XBR"]] #image[y_start:y_end,x_coordinate_start:x_coordinate_end](873, 415), (917, 432)
    cropped_bpm = frame[bpmCor["YTL"]:bpmCor["YBR"],bpmCor["XTL"]:bpmCor["XBR"]]
    cropped_spo2 = frame[spo2Cor["YTL"]:spo2Cor["YBR"],spo2Cor["XTL"]:spo2Cor["XBR"]]
    cropped_pr = frame[prCor["YTL"]:prCor["YBR"],prCor["XTL"]:prCor["XBR"]]
    cropped_resp = frame[respCor["YTL"]:respCor["YBR"],respCor["XTL"]:respCor["XBR"]]
    cropped_blood_pressure = frame[bloodPressureCor["YTL"]:bloodPressureCor["YBR"],bloodPressureCor["XTL"]:bloodPressureCor["XBR"]]
    cropped_mmHg = frame[mmHgCor["YTL"]:mmHgCor["YBR"],mmHgCor["XTL"]:mmHgCor["XBR"]]
    #cv2.imshow("cropped_temp", cropped_temp)
    # Converting to gray image
    gray_temp = cv2.cvtColor(cropped_temp, cv2.COLOR_BGR2GRAY)
    gray_bpm = cv2.cvtColor(cropped_bpm, cv2.COLOR_BGR2GRAY)
    gray_spo2 = cv2.cvtColor(cropped_spo2, cv2.COLOR_BGR2GRAY)
    gray_pr = cv2.cvtColor(cropped_pr, cv2.COLOR_BGR2GRAY)
    gray_resp = cv2.cvtColor(cropped_resp, cv2.COLOR_BGR2GRAY)
    gray_blood_pressure = cv2.cvtColor(cropped_blood_pressure, cv2.COLOR_BGR2GRAY)
    gray_mmHg = cv2.cvtColor(cropped_mmHg, cv2.COLOR_BGR2GRAY)
    
    
    #blurred_temp = cv2.GaussianBlur(gray_temp, (7, 7), 0)
    #cv2.imshow('blurred_temp',blurred_temp)
    #Converting gray image to binary
    
    (T, threshInv) = cv2.threshold(gray_temp, 0, 255,
	cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    
    cv2.imshow("Threshold", threshInv)
    print("[INFO] otsu's thresholding value: {}".format(T))
    
    thresh = 180
    binary_temp = cv2.threshold(gray_temp, thresh, 255, cv2.THRESH_BINARY)[1]
    binary_bpm = cv2.threshold(gray_bpm, thresh, 255, cv2.THRESH_BINARY)[1]
    binary_spo2 = cv2.threshold(gray_spo2, thresh, 255, cv2.THRESH_BINARY)[1]
    binary_pr = cv2.threshold(gray_pr, thresh, 255, cv2.THRESH_BINARY)[1]
    binary_resp = cv2.threshold(gray_resp, thresh, 255, cv2.THRESH_BINARY)[1]
    binary_blood_pressure = cv2.threshold(gray_blood_pressure, thresh, 255, cv2.THRESH_BINARY)[1]
    binary_mmHg = cv2.threshold(gray_mmHg, thresh, 255, cv2.THRESH_BINARY)[1]
    cv2.imshow('binary_temp_manual',binary_temp)
    
    #cv2.imshow('temp', cropped_temp)
    #cv2.imshow('bpm', cropped_bpm)
    #cv2.imshow('spo2', cropped_spo2)
    #cv2.imshow('pr', cropped_pr)
    #cv2.imshow('resp', cropped_resp)
    #cv2.imshow('bloodPressure', cropped_blood_pressure)
    #cv2.imshow('mmHg', cropped_mmHg)
    
    
    #cv2.imshow('binary_temp', binary_temp)
    #cv2.imshow('binary_bpm', binary_bpm)
    #cv2.imshow('binary_spo2', binary_spo2)
    #cv2.imshow('binary_pr', binary_pr)
    #cv2.imshow('binary_resp', binary_resp)
    #cv2.imshow('binary_blood_pressure', binary_blood_pressure)
    #cv2.imshow('binary_mmHg', binary_mmHg)
    
    
    filter = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
    # Applying cv2.filter2D function on our Logo image
    sharpen_img_2=cv2.filter2D(cropped_temp,-1,filter)
    #cv2.imshow('scaled_up_temp',sharpen_img_2)
    
    
    
    scale_up_x = 2.6
    scale_up_y = 2.6
    scaled_up_temp = cv2.resize(gray_temp , None, fx= scale_up_x, fy= scale_up_y, interpolation= cv2.INTER_LINEAR)
    cv2.imshow('scaled_up_temp',scaled_up_temp)
    
    
    filter = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
    # Applying cv2.filter2D function on our Logo image
    sharpen_img_2 = cv2.filter2D(scaled_up_temp,-1,filter)
    cv2.imshow('scaled_up_temp',sharpen_img_2)
    
    temp = reader.readtext(scaled_up_temp, batch_size=5)
    bpm = reader.readtext(cropped_bpm, batch_size=5)
    spo2 = reader.readtext(cropped_spo2, batch_size=5)
    pr = reader.readtext(cropped_pr, batch_size=5)
    resp = reader.readtext(cropped_resp, batch_size=5)
    blood_pressure = reader.readtext(cropped_blood_pressure, batch_size=5)
    mmHg = reader.readtext(cropped_mmHg, batch_size=5)
    '''
   
    '''
    #Draw Rectangle
    #frame = cv2.rectangle(frame, start_point_top_left_coordinate, end_point_bottom_right_coordinate, color, thickness)
    temp_rectangle = cv2.rectangle(frame, (tempCor["XTL"], tempCor["YTL"]), (tempCor["XBR"], tempCor["YBR"]), blue_color, thinckness_box)
    bpm_rectangle = cv2.rectangle(frame, (bpmCor["XTL"], bpmCor["YTL"]), (bpmCor["XBR"], bpmCor["YBR"]), blue_color, thinckness_box)
    spo2_rectangle = cv2.rectangle(frame, (spo2Cor["XTL"], spo2Cor["YTL"]), (spo2Cor["XBR"], spo2Cor["YBR"]), blue_color, thinckness_box)
    pr_rectangle = cv2.rectangle(frame, (prCor["XTL"],  prCor["YTL"]), (prCor["XBR"], prCor["YBR"]), blue_color, thinckness_box)
    resp_rectangle = cv2.rectangle(frame, (respCor["XTL"],respCor["YTL"]), (respCor["XBR"], respCor["YBR"]), blue_color, thinckness_box)
    blood_pressure_rectangle = cv2.rectangle(frame, (bloodPressureCor["XTL"],bloodPressureCor["YTL"]), (bloodPressureCor["XBR"], bloodPressureCor["YBR"]), blue_color, thinckness_box)
    mmHg_rectangle = cv2.rectangle(frame, (mmHgCor["XTL"], mmHgCor["YTL"]), (mmHgCor["XBR"], mmHgCor["YBR"]), blue_color, thinckness_box)
    #cv2.imshow('image', frame) 
  
    # Maintain output window utill
    # user presses a key
    #cv2.waitKey(0)        
  
    # Destroying present windows on screen
    #cv2.destroyAllWindows() 
    # Put Text
    # temp put text
    font = cv2.FONT_HERSHEY_SIMPLEX
    color = (0, 0, 255)
    thinckness = 2
    fontScale = 0.7
   
    
    # Making String to store data after checking if the list is empty or not
    # "{:.2f}".format(temp[0][-1])
    if len(temp) == 0:
        temp_print = 'Temp: Invalid'
    else:
        temp_print = 'temp: ' + str(temp[0][-2]) + ' ,C:' + str("{:.2f}".format(temp[0][-1]))
        
    if len(bpm) == 0:
        bpm_print = 'bpm: Invalid'
    else:
        bpm_print = 'bpm: ' + str(bpm[0][-2]) + ' ,C: ' + str("{:.2f}".format(bpm[0][-1]))
        
    if len(spo2) == 0:
        spo2_print = 'spo2: Invalid'
    else:
        spo2_print = 'spo2: ' + str(spo2[0][-2]) + ' C:  ' + str("{:.2f}".format(spo2[0][-1]))
       
    if len(pr) == 0:
        pr_print = 'pr: Invalid'
    else:
        pr_print = 'pr: ' + str(pr[0][-2]) + ' C:  ' + str("{:.2f}".format(pr[0][-1]))    
    
    if len(resp) == 0:
        resp_print = 'resp: Invalid'
    else:
        resp_print = 'resp: ' + str(resp[0][-2]) + ' C:  ' + str("{:.2f}".format(resp[0][-1])) 
    
    if len(blood_pressure) == 0:
        blood_pressure_print = 'blood_pressure: Invalid'
    else:
        blood_pressure_print = 'blood_pressure: ' + str(blood_pressure[0][-2]) + '  C: ' + str("{:.2f}".format(blood_pressure[0][-1]))
        
    if len(mmHg) == 0:
        mmHg_print = 'mmHg: Invalid'
    else:
        mmHg_print = 'mmHg: ' + str(mmHg[0][-2]) + ' C:  ' + str("{:.2f}".format(mmHg[0][-1]))    
    
    try:
        cv2.putText(frame, temp_print, (tempCor["XTL"] - 40,tempCor["YBR"] + 18), font, fontScale, color, thinckness, cv2.LINE_AA)
        cv2.putText(frame, bpm_print, (bpmCor["XTL"], bpmCor["YBR"] + 18), font, fontScale, color, thinckness, cv2.LINE_AA)
        cv2.putText(frame, spo2_print, (spo2Cor["XTL"], spo2Cor["YBR"] + 19), font, fontScale, color, thinckness, cv2.LINE_AA)
        cv2.putText(frame, pr_print, (prCor["XTL"], prCor["YBR"] + 18), font, fontScale, color, thinckness, cv2.LINE_AA)
        cv2.putText(frame, resp_print, (respCor["XTL"], respCor["YBR"] + 40), font, fontScale, color, thinckness, cv2.LINE_AA)
        cv2.putText(frame, blood_pressure_print, (bloodPressureCor["XTL"], bloodPressureCor["YTL"] - 20), font, fontScale, color, thinckness, cv2.LINE_AA)
        cv2.putText(frame, mmHg_print, (mmHgCor["XTL"], mmHgCor["YBR"] + 18), font, fontScale, color, thinckness, cv2.LINE_AA)
    except:
        print('Put Text Error')
    
    
    
    print('Patient Monitor OCR Result:')
    
    print(temp_print)
    print(bpm_print)
    print(spo2_print)
    print(pr_print)
    print(resp_print)
    print(blood_pressure_print)
    print(mmHg_print)
    print('    ')
    
    #end_time = datetime.now()
    #loop_time = 'Loop_Time: ' + str(end_time- start_time)
    #now = datetime.now() # current date and time
    #dateTime = now.strftime("%d-%m-%Y  Time-%H:%M:%S ")
    
    #webhook_print = '--------------------' + '\n' + 'Patient Monitor OCR Result:'+ '\n' + 'System Time: ' + dateTime +'\n' +temp_print + '\n' + bpm_print + '\n' + spo2_print + '\n' + pr_print + '\n' + resp_print + '\n' + blood_pressure_print + '\n' + mmHg_print + '\n' + loop_time + '\n' + '\n' 
    #print(webhook_print)
    
    #webhook = DiscordWebhook(url=discordWebhookUrl, content= webhook_print) #jlcpcbWebsite[0][8:] means remove first 8 character 
    #webhook.execute()
    #time.sleep(12)
    cv2.imshow('Frame', frame)
    # Press Q on keyboard to  exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
      break
#media_player.stop()