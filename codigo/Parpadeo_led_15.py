# Hacemos que el LED de la placa parpadee cada 1 segundo
from machine import Pin  # Importamos Pin del módulo machine
import time    # Importamos el módulo time completo
led = Pin('LED', Pin.OUT) # Configuramos GPIO15 como salida
while True:
    led.on()            # Encendemos
    time.sleep(1)  # Esperamos 1 segundo
    led.off()            # Apagamos
    time.sleep(1)  # Esperamos 1 segundo