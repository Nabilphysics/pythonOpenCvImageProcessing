import vlc
import cv2
import easyocr
import datetime

reader = easyocr.Reader(['en'], gpu = False)   

import time

directory = "C://Users/User/Desktop/PythonCode/openCvPractice/snapshot/snapshot"  
# creating vlc media player object
media_player = vlc.MediaPlayer()
  
# media object
#media = vlc.Media("http://tamperehacklab.tunk.org:38001/nphMotionJpeg?Resolution=640x480&Quality=Clarity")
media = vlc.Media("PatientMonitor5.mp4")
  
# setting media to the media player
media_player.set_media(media)
  
# setting video scale
#media_player.video_set_scale(1)
  
# start playing video
media_player.play()
  
# wait so the video can be played for 5 seconds
# irrespective for length of video
time.sleep(5)

path = directory + 'nabil.png'

while True:  
# taking screen shot
    media_player.video_take_snapshot(0,path, 0, 0)
    frame = cv2.imread('g4g.png') 
    time.sleep(10)
#media_player.stop()