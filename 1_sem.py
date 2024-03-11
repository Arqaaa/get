import RPi.GPIO as gp
import time

gp.setmode(gp.BCM)
gp.setup(14 ,gp.OUT)
gp.output(14 , 1)



