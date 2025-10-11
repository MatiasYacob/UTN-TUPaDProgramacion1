# imports
import random

# =========================#
# Helpers de validación
# me canse de errar inputs y tener que reiniciar el programa!!!
# =========================#
def input_str(prompt, allow_empty=False):
    while True:
        s = input(prompt)
        if s is None:
            s = ""
        s = s.strip()
        if s or allow_empty:
            return s
        print("[!] Entrada vacía. Intente nuevamente.")

def input_float(prompt, min_value=None, max_value=None):
    while True:
        s = input(prompt).strip()
        try:
            v = float(s.replace(",", "."))
        except ValueError:
            print("[!] Debe ingresar un número (use punto o coma para decimales).")
            continue
        if min_value is not None and v < min_value:
            print(f"[!] El valor no puede ser menor que {min_value}.")
            continue
        if max_value is not None and v > max_value:
            print(f"[!] El valor no puede ser mayor que {max_value}.")
            continue
        return v

def input_int(prompt, min_value=None, max_value=None):
    while True:
        s = input(prompt).strip()
        if not s or any(ch not in "+-0123456789" for ch in s):
            print("[!] Debe ingresar un número entero válido.")
            continue
        try:
            v = int(s)
        except ValueError:
            print("[!] Entero inválido.")
            continue
        if min_value is not None and v < min_value:
            print(f"[!] El valor no puede ser menor que {min_value}.")
            continue
        if max_value is not None and v > max_value:
            print(f"[!] El valor no puede ser mayor que {max_value}.")
            continue
        return v

def input_opcion(prompt, opciones_validas):
    """Devuelve la opción en minúscula si es válida (por ejemplo: {'a','q','salir'})"""
    opciones_lower = {o.lower() for o in opciones_validas}
    while True:
        s = input(prompt).strip().lower()
        if s in opciones_lower:
            return s
        print(f"[!] Opción inválida. Opciones válidas: {sorted(opciones_lower)}")

# =========================#
# 1) Promedio Notas de Estudiantes
# =========================#
notas = [7.5, 8.0, 6.3, 9.2, 4.5, 10.0, 5.8, 7.0, 8.7, 6.9]

for i in range(len(notas)):
    print(f"[1] Estudiante {i+1}: {notas[i]}")
promedio = sum(notas) / len(notas)
print("[1] Promedio:", round(promedio, 2))
nota_max = max(notas)
print("[1] Nota más alta:", nota_max)
nota_min = min(notas)
print("[1] Nota más baja:", nota_min)

# ========================= #
# 2) 5 productos en una lista (validado)
# ========================= #
productos = []
for i in range(5):
    producto = input_str(f"\n[2] Ingrese el nombre del producto {i+1}: ")
    productos.append(producto)

productos.sort(key=lambda x: x.lower())
print("[2] Productos ordenados alfabéticamente:")
for p in productos:
    print(f"[2] - {p}")

producto_borrar = input_str("\n[2] Ingrese el nombre del producto a borrar: ")
# Borrado case-insensitive
indice = next((idx for idx, val in enumerate(productos) if val.lower() == producto_borrar.lower()), -1)
if indice != -1:
    eliminado = productos.pop(indice)
    print(f"[2] Producto '{eliminado}' eliminado.")
else:
    print(f"[2] Producto '{producto_borrar}' no encontrado en la lista.")

print("[2] Lista actualizada de productos:")
for p in productos:
    print(f"[2] - {p}")

# ========================= #
# 3) lista con 15 números enteros al azar entre 1 y 100. (impresión con bucles)
# ========================= #
numeros = [random.randint(1, 100) for _ in range(15)]
numeros_pares = [num for num in numeros if num % 2 == 0]
numeros_impares = [num for num in numeros if num % 2 != 0]

print("\n[3] Números generados (uno por línea):")
for n in numeros:
    print(f"[3] {n}")

print("\n[3] Cantidad de numeros TOTAL:", len(numeros))
print("[3] Cantidad de numeros PARES:", len(numeros_pares))
print("[3] Cantidad de numeros IMPARES:", len(numeros_impares))

# ========================= #
# 4) lista con valores repetidos (impresión con bucles)
# ========================= #
datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
datos_sin_repetidos = list(set(datos))

print("\n[4] Lista original (uno por línea):")
for x in datos:
    print(f"[4] {x}")

print("[4] Lista sin duplicados (uno por línea):")
for x in datos_sin_repetidos:
    print(f"[4] {x}")

# ========================= #
# 5) Agregar o quitar nombres de una lista de estudiantes (validado)
# ========================= #
estudiantes = ["Ana", "Luis", "Carlos", "Marta", "Sofía", "Jorge", "Lucía", "Diego"]
print("\n[5] Lista inicial de estudiantes:")
for estudiante in estudiantes:
    print(f"[5] - {estudiante}")

while True:
    opcion = input_opcion("\n[5] ¿Desea agregar (a) o quitar (q) un estudiante? (o 'salir' para terminar): ", {"a", "q", "salir"})
    if opcion == 'salir':
        break
    elif opcion == 'a':
        nuevo_estudiante = input_str("[5] Ingrese el nombre del nuevo estudiante: ")
        estudiantes.append(nuevo_estudiante)
        print(f"[5] Estudiante '{nuevo_estudiante}' agregado.")
    elif opcion == 'q':
        estudiante_borrar = input_str("[5] Ingrese el nombre del estudiante a quitar: ")
        # Borrado case-insensitive
        idx = next((i for i, val in enumerate(estudiantes) if val.lower() == estudiante_borrar.lower()), -1)
        if idx != -1:
            eliminado = estudiantes.pop(idx)
            print(f"[5] Estudiante '{eliminado}' eliminado.")
        else:
            print(f"[5] Estudiante '{estudiante_borrar}' no encontrado en la lista.")

print("\n[5] Lista final de estudiantes:")
for estudiante in estudiantes:
    print(f"[5] - {estudiante}")

# ========================= #
# 6) Rotación de una lista 1 unidad a la derecha
# ========================= #
lista = [1, 2, 3, 4, 5, 6, 7]

print("\n[6] Lista original (uno por línea):")
for item in lista:
    print(f"[6] {item}")

lista_rotada = [lista[-1]] + lista[:-1]

print("[6] Lista rotada a la derecha (uno por línea):")
for item in lista_rotada:
    print(f"[6] {item}")

# ========================= #
# 7) Matriz 7x2 de temperaturas semanales
# ========================= 
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

temperaturas = []
print("\n[7] Ingrese las temperaturas mínimas y máximas de la semana:")
for i in range(7):
    t_min = input_float(f"[7] Temperatura mínima del {dias[i]}: ", min_value=-80, max_value=80)
    t_max = input_float(f"[7] Temperatura máxima del {dias[i]}: ", min_value=-80, max_value=80)
    if t_max < t_min:
        print("[7] Aviso: Máxima menor que mínima. Se intercambian los valores.")
        t_min, t_max = t_max, t_min
    temperaturas.append([t_min, t_max])

print("\n[7] Temperaturas registradas:")
for i in range(len(dias)):
    print(f"[7] {dias[i]} → Mín: {temperaturas[i][0]}°C | Máx: {temperaturas[i][1]}°C")

suma_min = 0.0
suma_max = 0.0
for fila in temperaturas:
    suma_min += fila[0]
    suma_max += fila[1]

promedio_min = suma_min / 7
promedio_max = suma_max / 7

amplitudes = []
for fila in temperaturas:
    amplitudes.append(fila[1] - fila[0])

max_amplitud = max(amplitudes)
dia_max_amplitud = dias[amplitudes.index(max_amplitud)]

print("\n[7] Promedio de temperaturas mínimas:", round(promedio_min, 2))
print("[7] Promedio de temperaturas máximas:", round(promedio_max, 2))
print(f"[7] Mayor amplitud térmica: {round(max_amplitud, 2)}°C, registrada el {dia_max_amplitud}.")

# ========================= #
# 8) Matriz con notas de 5 estudiantes en 3 materias (validado)
# ========================= #
estudiantes8 = ["Ana", "Luis", "Carlos", "Marta", "Sofía"]
materias8 = ["Matemática", "Lengua", "Programación"]

notas8 = []
print("\n[8] Ingrese las notas de los 5 estudiantes en 3 materias (0 a 10):")
for i in range(len(estudiantes8)):
    fila = []
    print(f"\n[8] Estudiante: {estudiantes8[i]}")
    for j in range(len(materias8)):
        nota = input_float(f"[8] Nota en {materias8[j]}: ", min_value=0, max_value=10)
        fila.append(nota)
    notas8.append(fila)

print("\n[8] Matriz de notas:")
for i in range(len(estudiantes8)):
    print(f"[8] {estudiantes8[i]}:", end=" ")
    for j in range(len(materias8)):
        print(f"{notas8[i][j]}", end="  ")
    print()

print("\n[8] Promedio de cada estudiante:")
for i in range(len(estudiantes8)):
    suma = 0.0
    for j in range(len(materias8)):
        suma += notas8[i][j]
    promedio_est = suma / len(materias8)
    print(f"[8] {estudiantes8[i]} → Promedio: {round(promedio_est, 2)}")

print("\n[8] Promedio de cada materia:")
for j in range(len(materias8)):
    suma = 0.0
    for i in range(len(estudiantes8)):
        suma += notas8[i][j]
    promedio_mat = suma / len(estudiantes8)
    print(f"[8] {materias8[j]} → Promedio: {round(promedio_mat, 2)}")

# ========================= #
# 9) Tablero de Ta-Te-Ti 
# ========================= #
print("\n[9] Bienvenidos al juego de Ta-Te-Ti")
tablero = [["-" for _ in range(3)] for _ in range(3)]

print("\n[9] Tablero inicial:")
for fila in tablero:
    for casilla in fila:
        print(casilla, end=" ")
    print()

def mostrar_tablero():
    print("\n[9] Estado actual del tablero:")
    for fila in tablero:
        for casilla in fila:
            print(casilla, end=" ")
        print()

jugadores = ["X", "O"]
turno = 0

while True:
    jugador = jugadores[turno % 2]
    print(f"\n[9] Turno del jugador {jugador}")
    fila = input_int("[9] Ingrese la fila (0, 1 o 2): ", 0, 2)
    columna = input_int("[9] Ingrese la columna (0, 1 o 2): ", 0, 2)

    if tablero[fila][columna] != "-":
        print("[9] Casilla ocupada. Elija otra.")
        continue

    tablero[fila][columna] = jugador
    mostrar_tablero()

    seguir = input_opcion("[9] ¿Desean seguir jugando? (s/n): ", {"s", "n"})
    if seguir != "s":
        print("\n[9] Juego finalizado. Tablero final:")
        mostrar_tablero()
        break

    turno += 1

# ========================= #
# 10) Ventas semanales de 4 productos durante 7 días 
# ========================= #
productos10 = ["Producto A", "Producto B", "Producto C", "Producto D"]
dias10 = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

ventas = []  # Matriz 4x7
print("\n[10] Ingrese las ventas de cada producto por día (>= 0):")
for i in range(len(productos10)):
    fila = []
    print(f"\n[10] {productos10[i]}:")
    for j in range(len(dias10)):
        venta = input_float(f"[10] Ventas del {dias10[j]}: ", min_value=0)
        fila.append(venta)
    ventas.append(fila)

print("\n[10] Matriz de ventas (productos x días):")
for i in range(len(productos10)):
    print(f"[10] {productos10[i]}:", end=" ")
    for j in range(len(dias10)):
        print(f"{ventas[i][j]}", end="  ")
    print()

print("\n[10] Total vendido por cada producto:")
totales_productos = []
for i in range(len(productos10)):
    total = 0.0
    for j in range(len(dias10)):
        total += ventas[i][j]
    totales_productos.append(total)
    print(f"[10] {productos10[i]} → Total semanal: {round(total, 2)}")

totales_dias = []
for j in range(len(dias10)):
    total_dia = 0.0
    for i in range(len(productos10)):
        total_dia += ventas[i][j]
    totales_dias.append(total_dia)

max_dia = max(totales_dias)
indice_max_dia = totales_dias.index(max_dia)
print(f"\n[10] Día con mayores ventas totales: {dias10[indice_max_dia]} ({round(max_dia, 2)} unidades)")

max_producto = max(totales_productos)
indice_max_producto = totales_productos.index(max_producto)
print(f"[10] Producto más vendido en la semana: {productos10[indice_max_producto]} ({round(max_producto, 2)} unidades)")

#===========================#
# Fin del programa
#===========================#
if __name__ == "__main__":
    print("\n[Fin] Programa finalizado.")
