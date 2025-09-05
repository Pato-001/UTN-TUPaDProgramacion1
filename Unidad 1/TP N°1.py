# Ejercicio 1

print('Hola Mundo!')


# Ejercicio 2

nombre=input('Ingrese su nombre:')
print(f'Hola {nombre}!')


# Ejercicio 3

nombre=input('Ingrese su nombre: ')
apellido=input('Ingrese su apellido: ')
edad=input('Ingrese su edad: ')
domicilio=input ('Ingrese su domicilio: ')
print(f'Soy {nombre} {apellido}, tengo {edad} años y vivo en {domicilio}')

# Ejercicio 4

radio=float(input('ingrese el radio de su circulo: '))
area= 3.1416 * radio**2
perimetro= 2*3.1416*radio
print(f'El area del circulo es: {area}')
print(f'El perimetro del circulo es: {perimetro}')


# Ejercicio 5


segundos = int(input('Ingrese la cantidad de segundos: '))
horas = segundos / 3600
print (f'{segundos} segundos equivalen a {horas}')


# Ejercicio 6


num=int(input('Ingrese el numero que desea multiplicar: '))
print (f'{num} x 1 = {num * 1}')
print (f'{num} x 2 = {num * 2}')
print (f'{num} x 3 = {num * 3}')
print (f'{num} x 4 = {num * 4}')
print (f'{num} x 5 = {num * 5}')
print (f'{num} x 6 = {num * 6}')
print (f'{num} x 7 = {num * 7}')
print (f'{num} x 8 = {num * 8}')
print (f'{num} x 9 = {num * 9}')
print (f'{num} x 10 = {num * 10}')


# Ejercicio 7


num1 = int(input('Ingrese un numero entero distinto que 0:'))
num2 = int(input('Ingrese otro numero entero distinto que 0:'))

print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)

# Ejercicio 8


peso = float(input('Ingrese su peso en kg: '))
altura = float(input('Ingrese su altura en mts: '))

imc = peso / (altura)**2
print (f'Tu indice de masa corporal es {imc}')


# Ejercicio 9


celcius = float(input('Ingrese su temperatura en celcius: '))
fahrenheit = (9/5)*celcius+32
print (f'Su temperatura en fahrenheit es: {fahrenheit}')


# Ejercicio 10


num1 = int(input('ingrese el primer numero: '))
num2 = int(input('ingrese el segundo numero: '))
num3 = int(input('ingrese el tercer numero: '))

promedio = (num1+num2+num3)/3
print(f'El promedio de tus numeros es: {promedio}')