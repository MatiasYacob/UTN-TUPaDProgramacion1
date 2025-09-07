
suma = 0
rango = 10 #<---MUY RECOMENDABLE QUE SEA 10

for i in range(rango): # <-- Cantidad de números a ingresar
    intero = int(input(f"\n[9] Ingrese un número entero: (faltan {rango - i}) "))
    suma += intero
    media = suma / (i + 1)
    print(f"Suma actual: {suma}, Media actual: {media:.2f}")
