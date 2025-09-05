# Ejercicio 1

edad = int(input("Por favor, ingrese su edad en años: "))

if edad > 18:
  print("Es mayor de edad")
  
# Ejercicio 2

nota = float(input("Ingrese su nota: "))

if nota >= 6:
    print('Aprobado')
else:
    print('Desaprobado')

# Ejercicio 3

numero = int(input('Ingrese un numero entero: '))

if numero % 2 == 0:
    print('Ha ingresado un número par')
else:
    print('Por favor, ingresar un número par')

# Ejercicio 4

edad = int(input('Por favor, ingrese su edad: '))

if edad < 12:
  print("Niño/a")
elif 12 <= edad < 18:
  print("Adolescente")
elif 18 <= edad < 30:
  print("Adulto/a joven")
else:
  print("Adulto/a")

# Ejercicio 5

contrasena = input("Ingrese su contraseña: ")

if 8 <= len(contrasena) <= 14:
  print("Ha ingresado una contraseña correcta")
else:
  print("Ingrese una contraseña de entre 8 y 14 caracteres")

# Ejercicio 6

import random
from statistics import mode, median, mean

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

if media > mediana > moda:
  print("Sesgo positivo o a la derecha")
elif media < mediana < moda:
  print("Sesgo negativo o a la izquierda")
elif media == mediana == moda:
  print("Sin sesgo")
  print("No se puede determinar si esta distribución tiene sesgo o no")

# Ejercicio 7

frase = input("Ingrese una frase o palabra: ")

if frase[-1] in ("AEIOUaeiou"):
  print(f"{frase}!")
else:
  print(frase)

# Ejercicio 8

nombre = input("Por favor, ingrese su nombre: ")
print("""En este programa puede realizar cualquiera de las siguientes operaciones:
1. Si quiere su nombre en mayúsculas.
2. Si quiere su nombre en minúsculas.
3. Si quiere su nombre con la primera letra mayúscula.
""")
opcion = int(input("Ingrese el número de operación que desea realizar: "))

if opcion == 1:
  nombre_mayuscula = nombre.upper()
  print(nombre_mayuscula)
elif opcion == 2:
  nombre_minuscula = nombre.lower()
  print(nombre_minuscula)
elif opcion == 3:
  nombre_title = nombre.title()
  print(nombre_title)
else:
  print("Por favor, ingrese únicamente 1, 2 o 3")

# Ejercicio 9

magnitud_terremoto = float(input("Por favor, ingrese la magnitud del terremoto según la escala de Ritcher: "))

if magnitud_terremoto < 3:
  print("Muy leve")
elif 3 <= magnitud_terremoto < 4:
  print("Leve")
elif 4 <= magnitud_terremoto < 5:
  print("Moderado")
elif 5 <= magnitud_terremoto < 6:
  print("Fuerte")
elif 6 <= magnitud_terremoto < 7:
  print("Muy fuerte")
else:
  print("Extremo")

# Ejercicio 10

hemisferio = input("Por favor, ingrese el hemisferio (N/S): ")
hemisferio = hemisferio.lower()

mes = int(input("Por favor, ingrese el mes del año en números: "))

dia = int(input("Por favor, ingrese el día del mes en números: "))


if hemisferio == "s":
  if (mes == 12 and dia >= 21) or (mes in (1,2)) or (mes == 3 and dia <= 20):
    print("Verano")
  elif (mes == 3 and dia >= 21) or (mes in (4,5)) or (mes == 6 and dia <= 20):
    print("Otoño")
  elif (mes == 6 and dia >= 21) or (mes in (7,8)) or (mes == 9 and dia <= 20):
    print("Invierno")
  elif (mes == 9 and dia >= 21) or (mes in (10,11)) or (mes == 12 and dia <= 20):
    print("Primavera")
elif hemisferio == "n":
  if (mes == 12 and dia >= 21) or (mes in (1,2)) or (mes == 3 and dia <= 20):
    print("Invierno")
  elif (mes == 3 and dia >= 21) or (mes in (4,5)) or (mes == 6 and dia <= 20):
    print("Primavera")
  elif (mes == 6 and dia >= 21) or (mes in (7,8)) or (mes == 9 and dia <= 20):
    print("Verano")
  elif (mes == 9 and dia >= 21) or (mes in (10,11)) or (mes == 12 and dia <= 20):
    print("Otoño")