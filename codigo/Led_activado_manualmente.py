# Encendemos y apagamos el LED con un pulsador
from machine import Pin
# Configuramos GPIO 15 como salida
led = Pin(15, Pin.OUT)
# Configuramos GPIO14  como entrada
# y en estado bajo (Low/0) por defecto (PULL_DOWN)
boton = Pin(14, Pin.IN, Pin.PULL_DOWN)
while True:              # Bucle infinito
    if boton.value(): # Si Botón pulsado
        led.on()            # Encendemos el LED
    else:                     #  Si no
        led.off()           # Apagamos el LED
        
