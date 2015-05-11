#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time

## Drives one servo by giving the convenience method to turn it 
class ServoDriver:
	## initializes the driver for a server
	def __init__(self, address = 0x40, channel = 0):
		self.data = []
		self.server_channel = 0
		self.freq = 60
		self.pwm = PWM(0x40)
		self.servoMin = 150
		self.servoMax = 600
		self.pwm.setPWMFreq(self.freq)
		self.angle = 90 #centered in the beginning
		self.move_t_bin = 100 #milliseconds

	## sets the server to the given angle with 90 being centered
	def set_angle(self, angle):
		self.angle = angle
		self.pwm.setPWM(self.server_channel, 0, self.__angle_to_pulse(self.angle))
		
	## takes care of using the server's settings to transform the values	
	def __angle_to_pulse(self, angle):
		assert(angle >= 0 and angle <= 180)
		anglePercent = angle / 180.0
		return int(self.servoMin + (self.servoMax - self.servoMin) * anglePercent)

	## smooth turning to a given angle given the angular-velocity
	def smooth_move(self, angle, angular_v):
		constrain(angle, 0 , 180)
		constrain(angular_v, 0, 100)
		delta_angle = abs(self.angle - angle)
		t = delta_angle / angular_v * 1000 #milliseconds

	def __move_delta_angle_t(self, delta_angle, t):
		steps = t / self.move_t_bin
		stepSize = delta_angle / steps
		for step in range(0, steps):
			self.angle += stepSize
			self.set_angle(angle) # if necessary reduce processing time by working on the pulse directly
			time.sleep(self.move_t_bin)

def constrain(input, min, max):
	output = input
	if (input < min):
		output = min
	elif (input > max):
		output = max
	return output