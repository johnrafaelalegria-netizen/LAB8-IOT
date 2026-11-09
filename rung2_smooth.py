from machine import ADC, Pin, PWM
from time import sleep

adc = ADC(Pin(34))
adc.atten(ADC.ATTN_11DB)
pwm = PWM(Pin(25), freq=1000)

N = 16   # change to 1 and run again to compare

def read_avg(adc, n):
    total = 0
    for _ in range(n):
        total += adc.read_u16()
    return total // n

while True:
    pwm.duty_u16(read_avg(adc, N))
    sleep(0.05)