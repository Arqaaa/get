import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
dac = [6 , 12 , 5 , 0 , 1 ,7 ,11 , 8]
dac.reverse()
comp = 14
troyka = 13

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka , GPIO.OUT,initial = GPIO.HIGH)
GPIO.setup(comp,GPIO.IN)

def dec2bin(x):
    return [int(bit) for bit in bin(x)[2:].zfill(8)]

def adc():
    for value in range(256):
        bin = dec2bin(value)
        GPIO.output(dac , bin)
        time.sleep(0.007)
        comp_val = GPIO.input(comp)
        if comp_val == 1:
            return float(value)

try:
    while True:
        q = adc()
        if q is not None:
            v = (q / 255)*3.3
            print(q , v)
            time.sleep(0.01)
finally:
    GPIO.output(dac , GPIO.LOW)
    GPIO.cleanup()

