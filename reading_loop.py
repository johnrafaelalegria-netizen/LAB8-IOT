from machine import ADC, Pin
from time import sleep

adc = ADC(Pin(34))
adc.atten(ADC.ATTN_11DB)

DARK = 14800        
BRIGHT = 47000

def read_avg(adc, n=16):
    total = 0
    for _ in range(n):
        total += adc.read_u16()
    return total // n

def light_pct(raw):
    pct = (raw - DARK) / (BRIGHT - DARK) * 100
    return max(0, min(100, pct))

while True:
    raw = read_avg(adc)
    pct = light_pct(raw)
    print(f"raw={raw:5d}   light={pct:.1f}")
sleep(0.2)

