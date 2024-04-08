import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)

pwm =GPIO.PWM(21,100)

try:
    pwm.start(0)
    while True:
        duty = float(input())

        pwm.ChangeDutyCycle(duty)

        v = (duty/255)*3.3
        print(v)
finally:
    pwm.stop()
    GPIO.cleanup()