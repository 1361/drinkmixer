import RPi.GPIO as GPIO
import time
import sys
import json
GPIO.setmode(GPIO.BOARD)
with open('/tmp/json-file') as data_file:
        data = json.load(data_file)

x1 = int(data)



def whiskey(x):
	GPIO.setup(x, GPIO.OUT)
	GPIO.output(x, GPIO.LOW)
	time.sleep(1.2)
	GPIO.output(x, GPIO.HIGH)
	GPIO.cleanup()


whiskey(x1)
print 'whiskey poured'
