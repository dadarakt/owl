from servoDriver import ServoDriver
import time

servoDriver = ServoDriver()
while True:
	servoDriver.setAngle(90)
	time.sleep(1)
	servoDriver.setAngle(0)
	time.sleep(1)
	servoDriver.setAngle(180)
	time.sleep(1)
