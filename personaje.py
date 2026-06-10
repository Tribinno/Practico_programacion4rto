from perosonaje import perosnaje
personaje  = []
menu = '''
1 - Ingresar participante
2 - Mostrar participantes
3 - Correr carrera
4 - Recuperar participantes
5 - Salir
'''
personaje = []

from perosonaje import perosnaje
personaje  = []
menu = '''
1 - Ingresar participante
2 - Mostrar participantes
3 - Correr carrera
4 - Recuperar participantes
5 - Salir
'''
personaje = []

while True:
    print(menu)

    opcion = int(input("seleccionar una opcion"))
    if opcion == 1:
        print("CREAR PERSONAJE") 

        nombre = input("ingresar el nombre del personaje")
        altura = int(input("ingresar la altura del personaje"))
        velocidad = float(input("ingresar la velocidad del personaje"))
        resistencia = int(input("ingresar la resistencia del perosnaje"))
        fuerza = int(input("ingresar la fuerza del peronaje"))

        perosnaje1=personaje(nombre, altura, velocidad, resistencia, fuerza)
        print(perosnaje1)

    elif opsion == 2:
        tiempo=perosnaje.corre(
        print("El personaje corrio", tiempo))
    
    elif opcion == 3
    break
   
