import sys
import time
import RPi.GPIO as GPIO
mode=GPIO.getmode()
Forward=37
Backward=38
sleeptime=1
GPIO.setmode(GPIO.BOARD)
GPIO.setup(Forward, GPIO.OUT)
GPIO.setup(Backward, GPIO.OUT)
def forward(x):
    GPIO.output(Forward, GPIO.HIGH)
    print("Moving Forward")
    time.sleep(x)
    GPIO.output(Forward, GPIO.LOW)
def reverse(x):
    GPIO.output(Backward, GPIO.HIGH)
    print("Moving Backward")
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Forward, GPIO.OUT)
    GPIO.setup(Backward, GPIO.OUT)
while(1):
    forward(5)
    reverse(5)
GPIO.cleanup()

