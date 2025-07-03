# Hacemos que el LED de la placa parpadee cada 1 segundo
from machine import Pin  # Importamos Pin del módulo machine
import time    # Importamos el módulo time completo
led15 = Pin(15, Pin.OUT) # Configuramos GPIO15 como salida
led_pico = Pin('LED', Pin.OUT) # Configuramos GPIO15 como salida
while True:
    print('LED Pico ON')  # Añadimos traza
    led_pico.on()   # Encendemos LED Pico
    print('LED 15 OFF')  # Añadimos traza
    led15.off()       # Apagamos LED 15  
    time.sleep(1)  # Esperamos 1 segundo
    print('LED Pico OFF')  # Añadimos traza
    led_pico.off()  # Apagamos LED Pico
    print('LED 15 ON')  # Añadimos trazas
    led15.on()        # Encendemos LED 15
    time.sleep(1)  # Esperamos 1 segundo