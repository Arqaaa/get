import RPi.GPIO as gp

gp.setmode(gp.BCM)
gp.setup(14 ,gp.IN)

gp.setup(18 ,gp.OUT)
gp.output(18 ,0)
gp.output(18 ,gp.input(14))
gp.cleanup()