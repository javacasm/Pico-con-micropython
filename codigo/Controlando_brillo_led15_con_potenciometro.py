# Controlamos el brillo de un LED con un potenciómetro
from machine import Pin, ADC, PWM
import time
# Configuramos GPIO26 como entrada analógica
pot = ADC(26)  # Medimos el voltaje del GPIO26 0 -65535
led = PWM(Pin(15))  # Controlamos el brillo del GPIO15
led.freq(500) 
while True:
    pot_valor = pot.read_u16() # Medimos el valor entre 0 y 65535 
    led.duty_u16(pot_valor)  # Damos el mismo valor de brillo
    print(3*pot_valor/65535,'V') # Imprimos el voltaje medido
    time.sleep(0.01)   
