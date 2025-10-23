#Ejercicio 1
def imprimir_hola_mundo():
    print("Hola Mundo!")
imprimir_hola_mundo()

#Ejercicio 2
def saludar_usuario(nombre):
    return f"Hola {nombre}!"
nombre = input("Ingrese su nombre: ")
print(saludar_usuario(nombre))

#Ejercicio 3
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")
informacion_personal(nombre, apellido, edad, residencia)

#Ejercicio 4
def calcular_area_circulo(radio):
    return 3.141592653589793 * radio * radio
def calcular_perimetro_circulo(radio):
    return 2 * 3.141592653589793 * radio
radio = float(input("Ingrese el radio del círculo: "))
print("Área del círculo:", calcular_area_circulo(radio))
print("Perímetro del círculo:", calcular_perimetro_circulo(radio))

#Ejercicio 5
def segundos_a_horas(segundos):
    return segundos / 3600
segundos = int(input("Ingrese la cantidad de segundos: "))
print("Horas:", segundos_a_horas(segundos))

#Ejercicio 6
def tabla_multiplicar(numero):
    for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))
tabla_multiplicar(numero)

#Ejercicio 7
def operaciones_basicas(a, b):
    return (a + b, a - b, a * b, a / b)
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
suma, resta, multiplicacion, division = operaciones_basicas(a, b)
print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)

#Ejercicio 8
def calcular_imc(peso, altura):
    return peso / (altura * altura)
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
imc = calcular_imc(peso, altura)
print(f"IMC: {imc:.2f}")

#Ejercicio 9
def celsius_a_fahrenheit(celsius):
    return celsius * 9 / 5 + 32
celsius = float(input("Ingrese la temperatura en Celsius: "))
print("Fahrenheit:", celsius_a_fahrenheit(celsius))

#Ejercicio 10
def calcular_promedio(a, b, c):
    return (a + b + c) / 3
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
c = float(input("Ingrese el tercer número: "))
print("Promedio:", calcular_promedio(a, b, c))