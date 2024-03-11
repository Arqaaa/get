import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
leds = [2 , 3 , 4 ,17, 27 , 22 ,10 , 9]
aux = [21 , 20 , 26 , 16 , 19, 25 , 23 , 24]
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(aux , GPIO.IN)
GPIO.output(leds , 1)

while True:
    for i in range(len(leds)):
        if GPIO.input(aux[i]) == 0:
            GPIO.output(leds[i] , 0)
        else:
            GPIO.output(leds[i] , 1)