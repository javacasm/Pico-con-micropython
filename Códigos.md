# Códigos micropython para Raspberry Pi Pico

## Programa de saludo por consola

```python
# Programa Saludo
# Pedimos al usuario la ciudad
# añadimos un espacio al final para separar la respuesta
ciudad = input('¿Dónde tienes tu clase hoy? ')
# Ahora usamos comillas dobles,
# se pueden usar simples ' o dobles " pero siempre emparejadas
nombre = input("¿Cómo te llamas? ")
# Si en print usamos , (una coma), se añade un espacio automáticamente para separar
# Si "sumamos" (concatenamos) las cadenas tenemos que añadir nosotros el espacio
print('Hola '+nombre+",",'Bienvenido a', ciudad)
```

## Encendemos el LED de la Pico durante 3 segundos

```python
# Encendemos el LED de la placa durante 3 segundos
from machine import Pin  # Importamos Pin del módulo machine
import time    # Importamos el módulo time completo
led = Pin('LED', Pin.OUT)  # Configuramos como salida
led.on()       # Encendemos
time.sleep(3)  # Esperamos 3 segundos
led.off()      # Apagamos
```

## Parpadeo del LED de la Pico

```python
# Hacemos que el LED de la placa parpadee cada 1 segundo
from machine import Pin  # Importamos Pin del módulo machine
import time    # Importamos el módulo time completo
led = Pin('LED', Pin.OUT) # Configuramos como salida
while True:
    led.on()       # Encendemos
    time.sleep(1)  # Esperamos 1 segundo
    led.off()      # Apagamos
    time.sleep(1)  # Esperamos 1 segundo
```

## Parpadeo del LED conectado a GPIO15

```python
# Hacemos que un led conectado a GPIO15  parpadee cada 1 segundo
from machine import Pin  # Importamos Pin del módulo machine
import time    # Importamos el módulo time completo
led = Pin(15, Pin.OUT)  # Configuramos GPIO15 como salida
while True:
	led.on()       # Encendemos
	time.sleep(1)  # Esperamos 1 segundo
	led.off()      # Apagamos
	time.sleep(1)  # Esperamos 1 segundo
```

## Alternamos los LED de la Pico y el conectado a GPIO 15

Añadimos trazas para ver en consola lo que debe verse en la placa

```python
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

```

## Encendemos y apagamos el LED con un pulsador

```python
# Encendemos y apagamos el LED con un pulsador
from machine import Pin
# Configuramos GPIO 15 como salida
led = Pin(15, Pin.OUT)
# Configuramos GPIO14  como entrada
# y en estado bajo (Low/0) por defecto (PULL_DOWN)
boton = Pin(14, Pin.IN, Pin.PULL_DOWN)
while True:         # Bucle infinito
    if boton.value(): # Si Botón pulsado
        led.on()          # Encendemos el LED
    else:             #  Si no
        led.off()         # Apagamos el LED
        
```

## Controlamos automáticamente el brillo del LED en GPIO15

Hacemos que suba el brillo desde el 0 (apagado) hasta el brillo máximo y luego lo bajamos hasta 0 otra ve


```python
from machine import Pin, PWM
led = PWM(Pin(15)) # Controlamos GPIO15 con PWM
led.freq(500)       # Usaremos un PWM de frecuencia 500Hz
# Primero subimos el brillo (Fade In)
for brillo in range(0, 65536): # desde 0 a 65535
    led.duty_u16(brillo)
# Bajamos el brillo (Fade Out)
for brillo in range(65535, -1,-1): # desde 65535 hasta 0
    led.duty_u16(brillo)    
```

## Controlamos el brillo del LED GPIO con un potenciómetro conectado a GPIO26

```python
from machine import Pin, ADC, PWM
import time
pot = ADC(26)  
led = PWM(Pin(15))  
led.freq(1000) 
while True:
    valor = pot.read_u16() 
    led.duty_u16(valor)  
    time.sleep(0.01)
```