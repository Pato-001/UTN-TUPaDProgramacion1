## 📦 Código del Programa de Gestión de Productos
# Este programa gestiona productos almacenados en un archivo de texto.

NOMBRE_ARCHIVO = "productos.txt"

def crear_archivo_inicial():
    """
    1. Crea el archivo inicial 'productos.txt' con tres productos.
       Cada línea tiene: nombre, precio, cantidad. (Actividad 1)
    """
    print("--- 1. Creando archivo inicial ---")
    
    # Datos iniciales (nombre,precio,cantidad)
    productos_iniciales = [
        "Lapicera,120.5,30",
        "Cuaderno A4,550.0,15",
        "Regla 30cm,85.75,50"
    ]
    
    # Usa 'w' (write) para crear y escribir, sobrescribiendo si existe.
    try:
        with open(NOMBRE_ARCHIVO, 'w') as archivo: # Aplicando with open() 
            for linea in productos_iniciales:
                archivo.write(linea + "\n")
        print(f"Archivo '{NOMBRE_ARCHIVO}' creado con éxito.")
    except IOError:
        print(f"Error al intentar crear el archivo '{NOMBRE_ARCHIVO}'.")


def cargar_productos_desde_archivo():
    """
    4. Lee el archivo y carga los datos en una lista de diccionarios. (Actividad 4)
    2. Muestra los productos en el formato solicitado. (Actividad 2)
    
    Retorna la lista de diccionarios o una lista vacía si falla la lectura.
    """
    productos_cargados = []
    print("\n--- 2. Leyendo y cargando productos ---")
    
    # Usa 'r' (read) para leer el archivo.
    try:
        with open(NOMBRE_ARCHIVO, 'r') as archivo: # Aplicando with open() 
            for linea in archivo:
                # Procesar la línea: .strip() y .split(",") 
                datos = linea.strip().split(",")
                
                if len(datos) == 3:
                    # Crear el diccionario (Actividad 4) 
                    try:
                        producto = {
                            "nombre": datos[0].strip(),
                            "precio": float(datos[1].strip()),
                            "cantidad": int(datos[2].strip())
                        }
                        productos_cargados.append(producto)
                        
                        # Mostrar en el formato solicitado (Actividad 2) 
                        print(f"Producto: {producto['nombre']} | Precio: ${producto['precio']:.2f} | Cantidad: {producto['cantidad']}")
                    except ValueError:
                        print(f"Advertencia: Error de formato en la línea: {linea.strip()}. Saltando.")
                else:
                    print(f"Advertencia: Línea incompleta o con formato incorrecto: {linea.strip()}. Saltando.")
        
        print(f"Se cargaron {len(productos_cargados)} productos en la lista.")
    except FileNotFoundError:
        print(f"Error: El archivo '{NOMBRE_ARCHIVO}' no existe. Ejecute la función de creación primero.")
    except IOError:
        print(f"Error al intentar leer el archivo '{NOMBRE_ARCHIVO}'.")
        
    return productos_cargados


def agregar_producto_desde_teclado():
    """
    3. Pide al usuario que ingrese un nuevo producto y lo agrega al archivo
       sin borrar el contenido existente. (Actividad 3)
    """
    print("\n--- 3. Agregando producto desde teclado ---")
    
    nombre = input("Ingrese el nombre del nuevo producto: ").strip()
    
    # Bucle para validar el precio como número (float)
    while True:
        try:
            precio = float(input("Ingrese el precio: ").strip())
            break
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un precio numérico.")

    # Bucle para validar la cantidad como número entero (int)
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad: ").strip())
            break
        except ValueError:
            print("Entrada inválida. Por favor, ingrese una cantidad entera.")

    # Formatea la nueva línea
    nueva_linea = f"{nombre},{precio},{cantidad}\n"
    
    # Usa 'a' (append) para agregar sin borrar el contenido existente. (Actividad 3) 
    try:
        with open(NOMBRE_ARCHIVO, 'a') as archivo:
            archivo.write(nueva_linea)
        print(f"El producto '{nombre}' ha sido agregado a '{NOMBRE_ARCHIVO}'.")
    except IOError:
        print(f"Error al intentar escribir en el archivo '{NOMBRE_ARCHIVO}'.")


def buscar_producto(productos):
    """
    5. Pide un nombre de producto, recorre la lista y muestra sus datos o un mensaje
       de error. (Actividad 5)
    """
    print("\n--- 4. Buscando producto por nombre ---")
    if not productos:
        print("La lista de productos está vacía. No se puede buscar.")
        return

    nombre_buscar = input("Ingrese el nombre del producto a buscar: ").strip().lower()
    encontrado = False
    
    for producto in productos:
        if producto["nombre"].lower() == nombre_buscar:
            print("\n¡Producto encontrado!")
            print(f"Nombre: {producto['nombre']}")
            print(f"Precio: ${producto['precio']:.2f}")
            print(f"Cantidad: {producto['cantidad']}")
            encontrado = True
            break
            
    if not encontrado:
        # Mostrar un mensaje de error si no existe (Actividad 5) [cite: 32]
        print(f"Error: Producto '{nombre_buscar}' no encontrado en la lista.")


def guardar_productos_actualizados(productos):
    """
    6. Sobrescribe el archivo 'productos.txt' con el contenido actual de la lista. (Actividad 6)
    """
    print("\n--- 5. Guardando productos actualizados ---")
    
    # Usa 'w' (write) para sobrescribir el archivo. (Actividad 6) 
    try:
        with open(NOMBRE_ARCHIVO, 'w') as archivo:
            for producto in productos:
                # Formato: nombre,precio,cantidad
                linea = f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n"
                archivo.write(linea)
        print(f"Archivo '{NOMBRE_ARCHIVO}' actualizado con {len(productos)} productos.")
    except IOError:
        print(f"Error al intentar guardar los productos en '{NOMBRE_ARCHIVO}'.")


def menu_principal():
    """Función principal para orquestar la ejecución del programa."""
    
    # 1. Crear el archivo inicial (si no existe o para reiniciar)
    crear_archivo_inicial()
    
    # 4. y 2. Leer y cargar la lista de productos
    productos_lista = cargar_productos_desde_archivo()
    
    # 3. Agregar un producto
    if productos_lista:
        agregar_producto_desde_teclado()

    # 4. Recargar la lista después de agregar, para tener el producto nuevo en memoria
    # Esta es una buena práctica para reflejar los cambios en el archivo.
    productos_lista = cargar_productos_desde_archivo()
    
    # 5. Buscar un producto
    buscar_producto(productos_lista)
    
    # 6. Guardar la lista actualizada (todos los productos, incluyendo el agregado)
    guardar_productos_actualizados(productos_lista)
    
    print("\nPrograma finalizado. ¡Pruebe su programa varias veces! [cite: 40]")


if __name__ == "__main__":
    menu_principal()