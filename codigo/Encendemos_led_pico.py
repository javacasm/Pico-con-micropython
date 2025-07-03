# Encendemos el LED de la placa durante 3 segundos
from machine import Pin  # Importamos Pin del módulo machine
import time    # Importamos el módulo time completo
led = Pin('LED', Pin.OUT) # Configuramos como salida
led.on()            # Encendemos
time.sleep(3)  # Esperamos 3 segundos
led.off()            # Apagamos