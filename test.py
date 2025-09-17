# 6) Rotación de una lista 1 unidad a la derecha
# =========================
lista = [1, 2, 3, 4, 5, 6, 7]

print("\n[6] Lista original:", lista)
lista_rotada = [lista[-1]] + lista[:-1]  # Rotar la lista una unidad a la derecha
print("[6] Lista rotada a la derecha:", lista_rotada)

# =========================