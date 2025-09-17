#imports   
import random




# =========================
# 1) Promedio Notas de Estudiantes
# =========================
notas = [7.5, 8.0, 6.3, 9.2, 4.5, 10.0, 5.8, 7.0, 8.7, 6.9]

for i in range(len(notas)):
    print(f"[1] Estudiante {i+1}: {notas[i]}")  # Mostrar la lista completa
promedio = sum(notas) / len(notas)  # Calcular el promedio
print("[1] Promedio:", promedio)
nota_max = max(notas)  # Nota más alta
print("[1] Nota más alta:", nota_max)
nota_min = min(notas)  # Nota más baja
print("[1] Nota más baja:", nota_min)

# =========================
# 2) 5 productos en una lista
# =========================
productos = []
for i in range(5):
    producto = input(f"\n[2] Ingrese el nombre del producto {i+1}: ")
    productos.append(producto)
productos.sort() #Ordernar la lista alfabéticamente
print("[2] Productos ordenados alfabéticamente:")
for producto in productos:
    print(producto)
producto_borrar = input("\n[2] Ingrese el nombre del producto a borrar: ") #Borrar un producto
if producto_borrar in productos:
    productos.remove(producto_borrar)
    print(f"[2] Producto '{producto_borrar}' eliminado.")
else:
    print(f"[2] Producto '{producto_borrar}' no encontrado en la lista.")
print("[2] Lista actualizada de productos:")
for producto in productos:
    print(producto)
    
# =========================
# 3) lista con 15 números enteros al azar entre 1 y 100.
# =========================
numeros = [random.randint(1, 100) for _ in range(15)]
numeros_pares = [num for num in numeros if num % 2 == 0]
numeros_impares = [num for num in numeros if num % 2 != 0]
print("\n[3] Números generados:", numeros)
print("\n[3] Cantidad de numeros TOTAL:", len(numeros))
print("[3] Cantidad de numeros PARES:", len(numeros_pares))
print("[3] Cantidad de numeros IMPARES:", len(numeros_impares))

# =========================
# 4)  lista con valores repetidos
# =========================
datos =[1, 3, 5, 3, 7, 1, 9, 5, 3]
datos_sin_repetidos = list(set(datos))  # Eliminar duplicados usando set
print("\n[4] Lista original:", datos)
print("[4] Lista sin duplicados:", datos_sin_repetidos)