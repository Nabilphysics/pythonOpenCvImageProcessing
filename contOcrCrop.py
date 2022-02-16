'''
Syed Razwanul Haque(Nabil)
Engineering Lead, Hardware Team, Bioforge Health Systems Ltd
'''

# importing libraries
import cv2
import easyocr
import datetime

reader = easyocr.Reader(['en'], gpu = False) 

font = cv2.FONT_HERSHEY_SIMPLEX

red_color = (0, 0, 255) #red
# Blue color in BGR
blue_color = (255, 0, 0)
thinckness_box = 2
fontScale = 0.7
   
# Create a VideoCapture object and read from input file
cap = cv2.VideoCapture('PatientMonitor5cutt.mp4')
   
# Check if camera opened successfully
if (cap.isOpened()== False): 
  print("Error opening video  file")
   
# Read until video is completed
while(cap.isOpened()):
  #cap = cv2.VideoCapture('PatientMonitor5cutt.mp4')   
  #cap.set(cv2.CAP_PROP_POS_MSEC,5000)
  cap = cv2.VideoCapture('http://tamperehacklab.tunk.org:38001/nphMotionJpeg?Resolution=640x480&Quality=Clarity')
  # Capture frame-by-frame
  start_time = datetime.datetime.now()
  ret, frame = cap.read()
  #h,w,c = frame.shape
  
  #print("Original Height ,Width and Channel:", h,"x", w, c)
  if ret == True:
   
    # Display the resulting frame
    #cv2.imshow('Frame', frame)
    
    
    # Cropping the point of interest to extract data
    #high Monitor Image Size
    cropped_temp = frame[415:432,873:917] #image[y_start:y_end,x_coordinate_start:x_coordinate_end]
    cropped_bpm = frame[153:261,762:991]
    cropped_spo2 = frame[315:372,754:861]
    cropped_pr = frame[312:356,959:1047]
    cropped_resp = frame[399:437,741:809]
    cropped_blood_pressure = frame[482:541,219:489]
    cropped_mmHg = frame[503:538,546:643]
    
    # Converting to gray image
    gray_temp = cv2.cvtColor(cropped_temp, cv2.COLOR_BGR2GRAY)
    gray_bpm = cv2.cvtColor(cropped_bpm, cv2.COLOR_BGR2GRAY)
    gray_spo2 = cv2.cvtColor(cropped_spo2, cv2.COLOR_BGR2GRAY)
    gray_pr = cv2.cvtColor(cropped_pr, cv2.COLOR_BGR2GRAY)
    gray_resp = cv2.cvtColor(cropped_resp, cv2.COLOR_BGR2GRAY)
    gray_blood_pressure = cv2.cvtColor(cropped_blood_pressure, cv2.COLOR_BGR2GRAY)
    gray_mmHg = cv2.cvtColor(cropped_mmHg, cv2.COLOR_BGR2GRAY)
    
    #Converting gray image to binary
    thresh = 65
    binary_temp = cv2.threshold(gray_temp, thresh, 255, cv2.THRESH_BINARY)[1]
    binary_bpm = cv2.threshold(gray_bpm, thresh, 255, cv2.THRESH_BINARY)[1]
    binary_spo2 = cv2.threshold(gray_spo2, thresh, 255, cv2.THRESH_BINARY)[1]
    binary_pr = cv2.threshold(gray_pr, thresh, 255, cv2.THRESH_BINARY)[1]
    binary_resp = cv2.threshold(gray_resp, thresh, 255, cv2.THRESH_BINARY)[1]
    binary_blood_pressure = cv2.threshold(gray_blood_pressure, thresh, 255, cv2.THRESH_BINARY)[1]
    binary_mmHg = cv2.threshold(gray_mmHg, thresh, 255, cv2.THRESH_BINARY)[1]
    
    '''
    cv2.imshow('temp', cropped_temp)
    cv2.imshow('bpm', cropped_bpm)
    cv2.imshow('spo2', cropped_spo2)
    cv2.imshow('pr', cropped_pr)
    cv2.imshow('resp', cropped_resp)
    cv2.imshow('bloodPressure', cropped_blood_pressure)
    cv2.imshow('mmHg', cropped_mmHg)
    '''
    
    cv2.imshow('binary_temp', binary_temp)
    cv2.imshow('binary_bpm', binary_bpm)
    cv2.imshow('binary_spo2', binary_spo2)
    cv2.imshow('binary_pr', binary_pr)
    cv2.imshow('binary_resp', binary_resp)
    cv2.imshow('binary_blood_pressure', binary_blood_pressure)
    cv2.imshow('binary_mmHg', binary_mmHg)
    
    
    temp = reader.readtext(binary_temp)
    bpm = reader.readtext(binary_bpm)
    spo2 = reader.readtext(binary_spo2)
    pr = reader.readtext(binary_pr)
    resp = reader.readtext(binary_resp)
    blood_pressure = reader.readtext(binary_blood_pressure)
    mmHg = reader.readtext(binary_mmHg)
    
    
    #Draw Rectangle
    #frame = cv2.rectangle(frame, start_point_top_left_coordinate, end_point_bottom_right_coordinate, color, thickness)
    temp_rectangle = cv2.rectangle(frame, (873, 415), (917, 432), blue_color, thinckness_box)
    bpm_rectangle = cv2.rectangle(frame, (762, 153), (991, 261), blue_color, thinckness_box)
    spo2_rectangle = cv2.rectangle(frame, (754, 315), (861, 372), blue_color, thinckness_box)
    pr_rectangle = cv2.rectangle(frame, (959,  312), (1047, 356), blue_color, thinckness_box)
    resp_rectangle = cv2.rectangle(frame, (741, 399), (809, 437), blue_color, thinckness_box)
    blood_pressure_rectangle = cv2.rectangle(frame, (219,482), (489, 541), blue_color, thinckness_box)
    mmHg_rectangle = cv2.rectangle(frame, (546, 503), (643, 538), blue_color, thinckness_box)
    
    # Put Text
    # temp put text
    font = cv2.FONT_HERSHEY_SIMPLEX
    color = (0, 0, 255)
    thinckness = 2
    fontScale = 0.7
    cv2.putText(frame, str(temp[0][-2]), (870,456), font, fontScale, color, thinckness, cv2.LINE_AA)
    cv2.putText(frame, str(bpm[0][-2]), (720, 235), font, fontScale, color, thinckness, cv2.LINE_AA)
    cv2.putText(frame, str(spo2[0][-2]), (760, 309), font, fontScale, color, thinckness, cv2.LINE_AA)
    cv2.putText(frame, str(pr[0][-2]), (959,  306), font, fontScale, color, thinckness, cv2.LINE_AA)
    cv2.putText(frame, str(resp[0][-2]), (760, 460), font, fontScale, color, thinckness, cv2.LINE_AA)
    cv2.putText(frame, str(blood_pressure[0][-2]), (350, 470), font, fontScale, color, thinckness, cv2.LINE_AA)
    cv2.putText(frame, str(mmHg[0][-2]), (555, 500), font, fontScale, color, thinckness, cv2.LINE_AA)
    
    
    # Making String to store data
    temp_print = 'temp: ' + str(temp[0][-2]) + ' Confidence: ' + str(temp[0][-1])
    bpm_print = 'bpm: ' + str(bpm[0][-2]) + ' Confidence: ' + str(bpm[0][-1])
    spo2_print = 'spo2: ' + str(spo2[0][-2]) + ' Confidence: ' + str(spo2[0][-1])
    pr_print = 'pr: ' + str(pr[0][-2]) + ' Confidence: ' + str(pr[0][-1])
    resp_print = 'resp: ' + str(resp[0][-2]) + ' Confidence: ' + str(resp[0][-1])
    blood_pressure_print = 'blood_pressure: ' + str(blood_pressure[0][-2]) + ' Confidence: ' + str(blood_pressure[0][-1])
    mmHg_print = 'mmHg: ' + str(mmHg[0][-2]) + ' Confidence: ' + str(mmHg[0][-1])
    
    
    
    print('Patient Monitor OCR Result:')
    print(temp_print)
    print(bpm_print)
    print(spo2_print)
    print(pr_print)
    print(resp_print)
    print(blood_pressure_print)
    print(mmHg_print)
    print('    ')
    end_time = datetime.datetime.now()
    print('Loop Time: ',end_time - start_time)
    cv2.imshow('Frame', frame)
    # Press Q on keyboard to  exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
      break
   
  # Break the loop
  else: 
    break
   
# When everything done, release 
# the video capture object
cap.release()
   
# Closes all the frames
cv2.destroyAllWindows()