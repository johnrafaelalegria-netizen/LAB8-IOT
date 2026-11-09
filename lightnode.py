from machine import ADC, Pin, PWM

class LightNode:
    def __init__(self, adc_pin, pwm_pin, dark, bright, n=16):
        self.adc = ADC(Pin(adc_pin))
        self.adc.atten(ADC.ATTN_11DB)
        self.pwm = PWM(Pin(pwm_pin), freq=1000)
        self.dark = dark
        self.bright = bright
        self.n = n

    def read_pct(self):
        total = 0
        for _ in range(self.n):
            total += self.adc.read_u16()
        raw = total // self.n
        pct = (raw - self.dark) / (self.bright - self.dark) * 100
        return max(0, min(100, pct))

    def set_brightness(self, pct):
        pct = max(0, min(100, pct))
        self.pwm.duty_u16(int(pct / 100 * 65535))

    def update(self):
        self.set_brightness(self.read_pct())