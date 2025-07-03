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