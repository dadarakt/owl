# imports
import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
from picamera.array import PiRGBArray
from picamera import PiCamera
import time 
import cv2

# setup camera
camera = PiCamera()
camera.resolution = (200, 200)
camera.start_preview()
rawCapture = PiRGBArray(camera)

#warmup camera (seems to be important)
time.sleep(0.1)

#get some image
camera.capture(rawCapture, format="bgr")
image = rawCapture.array

#and display it
aha = cv2.imwrite('testtest.jpg', image)
print aha
cv2.waitKey(0)
