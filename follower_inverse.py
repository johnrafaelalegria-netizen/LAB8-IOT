from machine import ADC, Pin, PWM
from time import sleep

adc = ADC(Pin(34))
adc.atten(ADC.ATTN_11DB)
pwm = PWM(Pin(25), freq=1000)

while True:
    raw = adc.read_u16()
    pwm.duty_u16(65535 - raw)
    sleep(0.05)