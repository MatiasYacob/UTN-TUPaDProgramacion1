import os # Para manejo de archivos y carpetas
import time  # Para simular tiempos de espera porque me parece divertido


#==========================#
# Utilidad: asegurar carpeta data
#==========================#
def asegurar_carpeta(ruta_archivo: str) -> None:
    carpeta = os.path.dirname(ruta_archivo)
    if carpeta:
        os.makedirs(carpeta, exist_ok=True)


#==========================#
# [1] Crear archivo productos.txt
#==========================#
def crear_archivo_inicial(ruta_archivo: str) -> None:
    asegurar_carpeta(ruta_archivo)

    lineas = [
        "Lapicera,120.5,30\n",
        "Cuaderno,450.0,15\n",
        "Goma,80.0,50\n"
    ]

    with open(ruta_archivo, "w", encoding="utf-8") as archivo:
        archivo.writelines(lineas)

    print("[1] Creando archivo productos.txt...")
    time.sleep(1)
    print("[1] Archivo productos.txt creado correctamente.\n")


#==========================#
# [2] Leer y mostrar productos desde el archivo
#==========================#
def mostrar_productos_desde_archivo(ruta_archivo: str) -> None:
    if not os.path.exists(ruta_archivo):
        print("[2] Error: el archivo productos.txt no existe. Cree el archivo primero con la opción [1].\n")
        return

    print("[2] Cargando productos...")
    time.sleep(1)

    with open(ruta_archivo, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            time.sleep(0.2)
            nombre, precio, cantidad = linea.strip().split(",")
            print(f"[2] • {nombre} | Precio: {precio} | Cantidad: {cantidad}")

    print("[2] Productos cargados correctamente.\n")


#==========================#
# [3] Agregar un nuevo producto
#==========================#
def agregar_producto(ruta_archivo: str, productos: list[dict] | None) -> None:
    if not os.path.exists(ruta_archivo):
        print("[3] Error: el archivo productos.txt no existe. Cree el archivo primero con la opción [1].\n")
        return

    # Mostrar productos actuales antes de preguntar el nuevo
    print("[3] Productos actuales:")
    time.sleep(0.5)

    with open(ruta_archivo, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            nombre, precio, cantidad = linea.strip().split(",")
            print(f"[3] • {nombre} | Precio: {precio} | Cantidad: {cantidad}")
            time.sleep(0.15)

    print()  # Espacio antes del input

    print("[3] Agregar un nuevo producto")
    time.sleep(1)

    nombre = input("[3] Ingrese el nombre del producto: ").strip()
    precio = input("[3] Ingrese el precio: ").strip()
    cantidad = input("[3] Ingrese la cantidad: ").strip()

    # Validaciones
    try:
        precio_f = float(precio)
        cantidad_i = int(cantidad)
    except ValueError:
        print("[3] Error: precio o cantidad inválidos.\n")
        return

    # Agregar al archivo
    with open(ruta_archivo, "a", encoding="utf-8") as archivo:
        archivo.write(f"{nombre},{precio_f},{cantidad_i}\n")

    # Actualizar lista en memoria si existe
    if productos is not None:
        productos.append({
            "nombre": nombre,
            "precio": precio_f,
            "cantidad": cantidad_i
        })

    print("[3] Guardando producto", end="", flush=True)
    for _ in range(3):
        time.sleep(0.4)
        print(".", end="", flush=True)

    print("\n[3] Producto agregado correctamente.\n")




#==========================#
# [4] Cargar productos en una lista de diccionarios
#==========================#
def cargar_productos_en_lista(ruta_archivo: str) -> list[dict]:
    productos: list[dict] = []

    if not os.path.exists(ruta_archivo):
        print("[4] Error: el archivo productos.txt no existe. Cree el archivo primero con la opción [1].\n")
        return productos

    print("[4] Cargando productos en la lista", end="", flush=True)
    for _ in range(3):
        time.sleep(0.3)
        print(".", end="", flush=True)
    print("\n")

    with open(ruta_archivo, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            nombre, precio, cantidad = linea.strip().split(",")
            productos.append({
                "nombre": nombre,
                "precio": float(precio),
                "cantidad": int(cantidad)
            })

    print(f"[4] Productos cargados en la lista: {len(productos)}")

    # Mostrar productos cargados
    for p in productos:
        time.sleep(0.2)
        print(f"[4] • {p['nombre']} | Precio: {p['precio']} | Cantidad: {p['cantidad']}")

    print()  # Salto de línea final
    return productos



#==========================#
# [5] Buscar producto por nombre (en la lista)
#==========================#
def buscar_producto_por_nombre(productos: list[dict] | None) -> None:
    if not productos:
        print("[5] No hay productos cargados en la lista. Use primero la opción [4].\n")
        return

    print("[5] Búsqueda de producto por nombre")
    time.sleep(1)

    nombre_buscar = input("[5] Ingrese el nombre del producto a buscar: ").strip()

    encontrado = False
    for producto in productos:
        if producto["nombre"].lower() == nombre_buscar.lower():
            print(f"[5] Producto encontrado:")
            print(f"    Nombre: {producto['nombre']}")
            print(f"    Precio: {producto['precio']}")
            print(f"    Cantidad: {producto['cantidad']}\n")
            encontrado = True
            break

    if not encontrado:
        print("[5] El producto no existe en la lista.\n")


#==========================#
# [6] Guardar lista de productos sobrescribiendo el archivo
#==========================#
def guardar_productos_en_archivo(ruta_archivo: str, productos: list[dict] | None) -> None:
    if not productos:
        print("[6] No hay productos en la lista para guardar. Use primero la opción [4] o agregue productos.\n")
        return

    asegurar_carpeta(ruta_archivo)

    print("[6] Guardando productos en el archivo", end="", flush=True)
    for _ in range(3):
        time.sleep(0.3)
        print(".", end="", flush=True)
    print()

    with open(ruta_archivo, "w", encoding="utf-8") as archivo:
        for p in productos:
            linea = f"{p['nombre']},{p['precio']},{p['cantidad']}\n"
            archivo.write(linea)

    print("[6] Archivo productos.txt sobrescrito con los datos de la lista.\n")


#==========================#
# Menú principal (sin variables globales)
#==========================#
def menu() -> None:
    ruta_archivo = "data/productos.txt"
    productos: list[dict] | None = None  # lista en memoria

    while True:
        print("====== MENÚ DE PRODUCTOS ======")
        print("[1] Crear archivo productos.txt inicial")
        print("[2] Mostrar productos desde el archivo")
        print("[3] Agregar producto (archivo y lista si está cargada)")
        print("[4] Cargar productos en una lista de diccionarios")
        print("[5] Buscar producto por nombre (en la lista)")
        print("[6] Guardar la lista de productos sobrescribiendo el archivo")
        print("[0] Salir")
        opcion = input("Seleccione una opción: ").strip()

        print()  # línea en blanco

        if opcion == "1":
            crear_archivo_inicial(ruta_archivo)
        elif opcion == "2":
            mostrar_productos_desde_archivo(ruta_archivo)
        elif opcion == "3":
            agregar_producto(ruta_archivo, productos)
        elif opcion == "4":
            productos = cargar_productos_en_lista(ruta_archivo)
        elif opcion == "5":
            buscar_producto_por_nombre(productos)
        elif opcion == "6":
            guardar_productos_en_archivo(ruta_archivo, productos)
        elif opcion == "0":
            print("Saliendo del programa...")
            time.sleep(1)
            break
        else:
            print("Opción inválida. Intente nuevamente.\n")


if __name__ == "__main__":
    menu()
