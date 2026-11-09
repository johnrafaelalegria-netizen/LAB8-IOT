from machine import ADC, Pin, PWM
from time import sleep

adc = ADC(Pin(34))
adc.atten(ADC.ATTN_11DB)
pwm = PWM(Pin(25), freq=1000)

DARK = 1800
BRIGHT = 52000
LOW = 30
HIGH = 40

def read_avg(adc, n=16):
    total = 0
    for _ in range(n):
        total += adc.read_u16()
    return total // n

def light_pct(raw):
    pct = (raw - DARK) / (BRIGHT - DARK) * 100
    return max(0, min(100, pct))

mode = "off"

while True:
    pct = light_pct(read_avg(adc))
    if mode == "off" and pct < LOW:
        mode = "on"
    elif mode == "on" and pct > HIGH:
        mode = "off"
    pwm.duty_u16(65535 if mode == "on" else 0)
    sleep(0.2)