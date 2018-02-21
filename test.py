import RPi.GPIO as GPIO
import time
import sys
GPIO.setmode(GPIO.BCM)

GPIO.setup(26, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)

GPIO.output(26, GPIO.LOW)
GPIO.output(19, GPIO.HIGH)
GPIO.output(13, GPIO.HIGH)
time.sleep(5)
GPIO.output(13, GPIO.LOW)
GPIO.output(19, GPIO.LOW)


GPIO.cleanup()
