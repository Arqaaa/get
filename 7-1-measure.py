import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt



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
GPIO.output(led , 0)

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
    q = 0
    data = []
    t_0 = time.time()
    k = 0
    GPIO.output(troyka , 1)

    while True:
        q = adc()
        data.append(q)
        time.sleep(0.01)
        L =q//32
        k += 1
        GPIO.output(led[:L] ,1)
        time.sleep(0.01)
        GPIO.output(led[:L] ,0)
        print(q)
        if q >= 256*0.8:
            break

    t = time.time() - t_0

    with open('/home/b04-305/Zahodov/get/data.txt' , 'w') as file:
        file.write('Измерение напряжения:' +'\n')
        for i in data:
            a = (i / 255)*3.3
            file.write(str(a) + '\n')
    with open('/home/b04-305/Zahodov/get/settings.txt' , 'w') as file:
        file.write('Средняя частота дискретизации:' + '\n' + str(1/t/k) + '\n')
        file.write('Шаг квантования:' + '\n' + '0.013' + '\n')


    y = [(a/256)*3.3 for a in data]
    x = [i*t/k for i in range(len(data))]
    plt.plot(x , y)
    plt.show()

finally:
    GPIO.output(dac , GPIO.LOW)
    GPIO.cleanup()


