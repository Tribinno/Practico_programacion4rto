from personajes import personaje 

#crear perosnaje
nombre = input("ingrese el nomre:")
altura = float(input("ingrese su altura"))
velicdad = float(input("ingrese su velocidad"))
resistencia = float(input("ingrese su resitencia"))
fuerza = float(input("ingrese su fuerza"))

perosnaje = personaje(nombre, altura, velocidad, resistencia, fuerza)

print("Datos del personaje:")
print(perosonaje.mostrar_datos)

# usar el metodo correr

distancia = float(input("ingrese la distancia a correr:"))

tiempo = perosnaje.correr(distancia)
print(tiempo)
