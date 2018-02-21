import RPi.GPIO as GPIO
import time
import sys
import json
GPIO.setmode(GPIO.BOARD)
with open('/tmp/coke') as data_file:
        data = json.load(data_file)

x1 = int(data)



def whiskey(x):
	GPIO.setup(x, GPIO.OUT)
	GPIO.output(x, GPIO.LOW)
	time.sleep(3)
	GPIO.output(x, GPIO.HIGH)
	GPIO.cleanup()


whiskey(x1)
print 'Coke poured'
