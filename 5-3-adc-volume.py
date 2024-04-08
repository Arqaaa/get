import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
dac = [6 , 12 , 5 , 0 , 1 ,7 ,11 , 8]
dac.reverse()
comp = 14
troyka = 13
led = [9 , 10 ,22,27,17,4,3,2]
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka , GPIO.OUT,initial = GPIO.HIGH)
GPIO.setup(comp,GPIO.IN)
GPIO.setup(led , GPIO.OUT)
def dec2bin(x):
    return [int(bit) for bit in bin(x)[2:].zfill(8)]

def adc():
    n = 0
    for i in range(7 , -1 , -1):
        n += 2**i
        bin = dec2bin(n)
        GPIO.output(dac , bin)
        time.sleep(0.007)
        comp_val = GPIO.input(comp)
        if comp_val == 1:
            n -= 2**i
    return n

try:
    while True:
        q = adc()
        if q is not None:
            v = (q / 255)*3.3
            print(q , v)
            time.sleep(0.01)
        q1 =q//32
        GPIO.output(led[:q1] ,1)
        time.sleep(0.01)
        GPIO.output(led[:q1] ,0)

finally:
    GPIO.output(dac , GPIO.LOW)
    GPIO.cleanup()

