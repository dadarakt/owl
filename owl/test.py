from servoDriver import ServoDriver
import time

servoDriver = ServoDriver()
while True:
	servoDriver.smooth_move(0, 50)
	servoDriver.smooth_move(90, 70)
	servoDriver.smooth_move(180, 100)
