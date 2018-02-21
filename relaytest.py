import RPi.GPIO as GPIO
import time
import sys
GPIO.setmode(GPIO.BOARD)

GPIO.setup(37, GPIO.OUT)
GPIO.setup(35, GPIO.OUT)

GPIO.output(37, GPIO.LOW)
time.sleep(3)
GPIO.output(37, GPIO.HIGH)




GPIO.cleanup()