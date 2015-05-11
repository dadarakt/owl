#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time

pwm = PWM(0x40)

servoMin = 150
servoMax = 600

pwm.setPWMFreq(60)

def setAngle(angle):
	print 'wurst'

while (True):
  # Change speed of continuous servo on channel O
  pwm.setPWM(0, 0, servoMin)
  time.sleep(2)
  pwm.setPWM(0, 0, servoMax)
  time.sleep(2)
