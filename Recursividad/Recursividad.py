# EJERCICIO 1: Factorial Recursivo
def factorial_recursivo(n):
    if n < 0:
        return "El factorial no está definido para números negativos."
    if n == 0:
        return 1
    else:
        return n * factorial_recursivo(n - 1)

def mostrar_factoriales():
    try:
        limite = int(input("Ingrese un número entero positivo para el límite (Factorial): "))
        if limite < 1:
            print("Por favor, ingrese un número mayor o igual a 1.")
            return

        print("\n--- Factoriales ---")
        for i in range(1, limite + 1):
            resultado = factorial_recursivo(i)
            print(f"El factorial de {i} ({i}!) es: {resultado}")
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número entero.")


# EJERCICIO 2: Serie de Fibonacci Recursiva
def fibonacci_recursivo(pos):
    if pos < 0:
        return "Posición inválida"
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    else:
        return fibonacci_recursivo(pos - 1) + fibonacci_recursivo(pos - 2)

def mostrar_serie_fibonacci():
    try:
        limite = int(input("Ingrese la posición límite para la serie de Fibonacci: "))
        if limite < 0:
            print("Por favor, ingrese un número positivo.")
            return

        serie = [fibonacci_recursivo(i) for i in range(limite + 1)]
        print(f"\nSerie de Fibonacci hasta la posición {limite}: {serie}")

    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número entero.")


# EJERCICIO 3: Potencia de un Número Recursiva
def potencia_recursiva(base, exponente):
    if exponente < 0:
        return "El exponente negativo no es compatible con esta fórmula recursiva simple."
    if exponente == 0:
        return 1
    else:
        return base * potencia_recursiva(base, exponente - 1)


# EJERCICIO 4: Conversión Decimal a Binario Recursiva
def decimal_a_binario_recursivo(decimal):
    if decimal == 0:
        return ""
    else:
        cociente = decimal // 2
        resto = decimal % 2
        return decimal_a_binario_recursivo(cociente) + str(resto)


# EJERCICIO 5: Palíndromo Recursivo
def es_palindromo(palabra):
    palabra = palabra.lower()
    if len(palabra) <= 1:
        return True
    if palabra[0] == palabra[-1]:
        return es_palindromo(palabra[1:-1])
    else:
        return False


# EJERCICIO 6: Suma de Dígitos Recursiva
def suma_digitos(n):
    if n < 0:
        return "Solo números positivos"
    if n == 0:
        return 0
    else:
        return (n % 10) + suma_digitos(n // 10)


# EJERCICIO 7: Conteo de Bloques en Pirámide Recursiva
def contar_bloques(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)


# EJERCICIO 8: Contar Dígito Recursiva
def contar_digito(numero, digito):
    if numero < 0 or not (0 <= digito <= 9):
        return "Entrada inválida"
    
    if numero == 0:
        return 0
    else:
        ultimo_digito = numero % 10
        resto_numero = numero // 10
        
        coincidencia = 1 if ultimo_digito == digito else 0
        
        return coincidencia + contar_digito(resto_numero, digito)


# --- PRUEBAS DE EJEMPLO DE USO (OPCIONAL) ---
print("\n--- EJEMPLOS DE USO DE LAS FUNCIONES ---")

# Prueba Ejercicio 1
print(f"1) Factorial de 5: {factorial_recursivo(5)}")

# Prueba Ejercicio 2
print(f"2) Fibonacci en posición 7: {fibonacci_recursivo(7)}")

# Prueba Ejercicio 3
print(f"3) Potencia 2^5: {potencia_recursiva(2, 5)}")

# Prueba Ejercicio 4
print(f"4) 10 en binario: {decimal_a_binario_recursivo(10)}")

# Prueba Ejercicio 5
print(f"5) 'Añora' es palíndromo?: {es_palindromo('añora')}")
print(f"5) 'Radar' es palíndromo?: {es_palindromo('radar')}")

# Prueba Ejercicio 6
print(f"6) Suma de dígitos de 1234: {suma_digitos(1234)}")

# Prueba Ejercicio 7
print(f"7) Bloques para base 4: {contar_bloques(4)}")

# Prueba Ejercicio 8
print(f"8) Veces que aparece 2 en 12233421: {contar_digito(12233421, 2)}")