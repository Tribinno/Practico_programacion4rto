#Crear una carpeta de trabajo, llamada "POO"
#Dentro de esa carpeta crear dos archivos .py uno llamado carrera.py y otro Personaje_clase.py
#En el archivo Personaje_clase.py desarrollar la clase Personaje  con
 #atributo de clase "estado = True" #vivo. Y el constructor y los atributos
  #(nombre, altura, velocidad, resistencia, fuerza)
 #y dos metodos, correr y recuperarse.
#Luego en el archivo carrera.py crear un menu: "ingresar participantes"
#pedirle los datos al usuario para instanciar objetos e imprimirlos por pantalla,
# "correr carrera" "pedir distancia" y realizar la carrera, "salir"

class personaje:
    estado = True

def __init__(self, nombre, altura, velocidad, resistencia, fuerza):
    self.nomber = nombre
    self.altura = altura
    self.velocidad = velocidad
    self.resistencia = resistencia
    self.fuerza = feurza    

def correr(self, distancia)
    if self.estado ==True:
    tiempo = distanica / self.velocidad

    # Pequeña modificación usando resistencia y fuerza
    # Si tiene poca resistencia, tarda un poco más 
    if self.resistencia    
