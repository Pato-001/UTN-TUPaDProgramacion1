#Ejercicio 1

for i in range (1,101):
    print(i)

#Ejercicio 2

num = int(input('Ingrese un número entero: '))
cant_digitos = 0

if num == 0:
    cant_digitos = 1
else:
    while num > 0:
        num = num // 10
        cant_digitos += 1

print(f'La cantidad de dígitos es de: {cant_digitos}')

#Ejercicio 3

num1 = int(input('Ingrese el primer numero entero: '))
num2 = int(input('Ingrese el segundo numero entero: '))

suma = 0

if num1 > num2:
    num1, num2 = num2, num1

for i in range (num1 + 1,num2):
        suma += i

print (f'La suma de los numeros comprendidos entre {num1} y {num2} es: {suma}')

#Ejercicio 4

suma = 0

num = int(input('Ingrese un numero entero: '))

while num != 0:
    suma += num
    num = int(input("Ingrese un numero mayor que cero: "))
    
print (f'La suma total es: {suma}')

#Ejercicio 5

import random

numero_secreto = random.randint(0, 9)

intentos = 0

while True:
    num = int(input('Ingrese un numero del 0 al 9: '))
    intentos += 1
    
    if num == numero_secreto:
        print(f'El numero es correcto, lo hiciste en {intentos} intentos')
        break
    else:
        print('El numero es incorrecto, segui intentando')

#Ejercicio 6

for i in range (100, 0,-2):
    print (i)

#Ejercicio 7

num = int(input("Ingrese un numero positivo entero: "))
suma_total = 0
for i in range (0, num, 1):
    suma_total += i

print(f'La suma entre 0 y los los numeros comprendidos entre el numero ingresado es: {suma_total}')

#Ejercicio 8

cantidad = 10

pares = 0
impares = 0
negativos = 0
positivos = 0

for i in range (cantidad):
    num = int(input(f'Ingrese el numero {i+1}: '))
    if num % 2 == 0:
        pares += 1
    else:
        impares +=1
        
    if num > 0:
        positivos += 1
    else:
        negativos += 1
        
print (f'La cantidad de numeros pares es de {pares}')
print (f'La cantidad de numeros impares es de {impares}')
print (f'La cantidad de numeros positivos es de {positivos}')
print (f'La cantidad de numeros negativos es de {negativos}')


#Ejercicio 9

cant = 10
suma = 0

for i in range (cant):
    num = int(input(f'Ingrese el numero {i+1}:'))
    suma += num
    
media = suma / cant

print (f'La media de los {cant} numeros es de {media}')

#Ejercicio 10

numero_ingresado10 = int(input("Ingrese un numero entero: "))

numero_invertido = int(str(numero_ingresado10)[::-1])

print(f"El número invertido es: {numero_invertido}")
