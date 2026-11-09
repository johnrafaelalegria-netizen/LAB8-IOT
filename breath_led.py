from machine import Pin, PWM
from time import sleep
pwm = PWM(Pin(25), freq=1000)
while True:
    for d in range(0, 65536, 1024):      
        pwm.duty_u16(d)
        sleep(0.02)
    for d in range(65535, -1, -1024):    
        pwm.duty_u16(d)
        sleep(0.02)