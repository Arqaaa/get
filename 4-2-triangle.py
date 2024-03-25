import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
dac = [6 , 12 , 5 , 0 , 1 ,7 ,11 , 8]
dac.reverse()
GPIO.setup(dac, GPIO.OUT)

def dec2bin(x):
    return [int(bit) for bit in bin(x)[2:].zfill(8)]


try:
    p = int(input())
    while True:
        for i in range(255):
            GPIO.output(dac,dec2bin(i))
            time.sleep(p/256)
        for i in range(255 , -1 , -1):
            GPIO.output(dac,dec2bin(i))
            time.sleep(p/256)

    
finally:
    GPIO.output(dac,0)
    GPIO.cleanup()