#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time

class ServoDriver:

	def __init__(self):
		self.data = []
		# constants which define the server dynamics given the frequency
		self.server_channel = 0
		self.freq = 60
		self.pwm = PWM(0x40)
		self.servoMin = 150
		self.servoMax = 600
		self.pwm.setPWMFreq(self.freq)


	def setAngle(self, angle):
		self.pwm.setPWM(self.server_channel, 0, self.__angleToPulse(angle))
		
	def __angleToPulse(self, angle):
		assert(angle >= 0 and angle <= 180)
		anglePercent = angle / 180.0
		return  int(self.servoMin + (self.servoMax - self.servoMin) * anglePercent)

