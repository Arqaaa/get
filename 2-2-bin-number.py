import RPi.GPIO as GPIO
import time

dac = [8 , 11 , 7 , 1 , 0 , 5 , 12 , 6]
numbers =[[1 , 1 ,1 ,1 ,1 ,1 ,1 ,1],
        [ 0 ,1 ,1 ,1 ,1 ,1 ,1 ,1],
        [0 ,1 ,0 ,0 ,0 ,0 ,0 ,0],
        [0 ,0 ,1 ,0 ,0 ,0 ,0 ,0],
        [0,0,0,0,0,1 ,0 ,1],
        [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
        [1, 0,0 ,0 ,0 ,0 ,0 , 0]]


GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
#number = [1, 0,0 ,0 ,0 ,0 ,0 , 0]
#GPIO.output(dac , number)
#time.sleep(10)

for i in numbers:
    GPIO.output(dac , i)
    time.sleep(10)


GPIO.output(dac , 0)
GPIO.cleanup()

#V:2.795 , 1.8 , 1.01 , 0.46 , 120*10^-3 , 053 , 1.68