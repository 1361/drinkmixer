import RPi.GPIO as GPIO
import time
import sys, json
GPIO.setmode(GPIO.BOARD)
with open('/tmp/json-file') as data_file:
        data = json.load(data_file)

x1 = int(data)

def setup(x):
	GPIO.setup(x, GPIO.OUT)
	GPIO.setup(37, GPIO.OUT)
	GPIO.output(x, GPIO.HIGH)
	time.sleep(1.2)
	GPIO.output(x, GPIO.LOW)
	GPIO.output(37, GPIO.HIGH)
	time.sleep(3)
	GPIO.output(37, GPIO.LOW)
	GPIO.cleanup()

print x1
setup(x1)
