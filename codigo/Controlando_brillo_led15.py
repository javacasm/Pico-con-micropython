from machine import Pin, PWM
led = PWM(Pin(15)) # Controlamos GPIO15 con PWM
led.freq(20)       # Usaremos un PWM de frecuencia 500Hz
# Primero subimos el brillo (Fade In)
for brillo in range(0, 65536): # desde 0 a 65535
    led.duty_u16(brillo)
# Bajamos el brillo (Fade Out)
for brillo in range(65535, -1,-1): # desde 65535 hasta 0
    led.duty_u16(brillo)  