# Ejemplo de uso de las HuskyLens desde la Pico usando micropython
# basado en el repositorio https://github.com/antonvh/PyHuskyLens/ de antonvh
# Adaptado por javacasm

from pyhuskylens import *
from machine import  Pin

from machine import SoftI2C,Pin
i2c = SoftI2C(scl=Pin(7),sda=Pin(6))

hl = HuskyLens(i2c,pwm=200,debug=False)

print(hl.get_version()) # This returns '.': OK and no payload on firmware < 0.5.1 > may not work

# Show some text on screen
hl.clear_text()
hl.show_text("Hola, soy la Pico", position=(120,120))

led = Pin('LED', Pin.OUT) # el led de la placa

def reconoce_caras():
    reconoce_cosas(ALGORITHM_FACE_RECOGNITION,'cara')
    
def reconoce_colores():
    reconoce_cosas(ALGORITHM_COLOR_RECOGNITION,'color')
    
def reconoce_cosas(algoritmo,nombre_cosa):
    print("Reconociendo ",nombre_cosa)
    hl.set_alg(algoritmo)

    while True:
        cosas = hl.get_blocks()
        hl.clear_text() # borramos la pantalla
        if len(cosas) > 0: # se ha detectado al menos 1 cosa
            hl.clear_text()
            for cosa in cosas: 
                cosa_encontrada = nombre_cosa 
                if cosa.ID != 0:  # Se ha identificado como algo memorizado
                    led.on()
                    cosa_encontrada += ':'+str(cosa.ID)
                else:
                    led.off()
                mensaje = f'{cosa_encontrada} {cosa.width}x{cosa.height}'
                print(mensaje, f'en ({cosa.x},{cosa.y})')
                hl.show_text(mensaje, position=(cosa.x,cosa.y)) # mostramos en la cámara la información
        else:
            led.off() # Apagamos el led porque no detectamos nada
            


reconoce_caras()  # ejecutamos el algoritmo de reconocimiento de caras

