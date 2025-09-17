import random

datos =[1, 3, 5, 3, 7, 1, 9, 5, 3]
datos_sin_repetidos = [list(set(datos))]  # Eliminar duplicados usando set
print("\n[4] Lista original:", datos)
print("[4] Lista sin duplicados:", datos_sin_repetidos)