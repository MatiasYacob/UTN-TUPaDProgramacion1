#=====================
#Imports de librerías
from statistics import mode, mean, median
import random
# ====================




# =========================
# 1) Numeros del 0 al 100 (enteros)
# =========================
for i in range(101):
    print(i)

# =========================
# 2) Cantidad de digitos de un numero
# =========================
numero = input("\n[2] Ingrese un número entero: ")
print(f"El número {numero} tiene {len(numero)} dígitos.")

# =========================
# 3) Sumar números comprendidos entre dos enteros
# =========================
numero1 = int(input("\n[3] Ingrese el primer número: "))
numero2 = int(input("\n[3] Ingrese el segundo número: "))
mayor = max(numero1, numero2)
menor = min(numero1, numero2)
suma = 0
for i in range(menor+1, mayor):
    suma += i
print(f"La suma de los números entre {menor} y {mayor} es: {suma}")

# =========================
# 4) Suma de enteros hasta que se ingrese un 0
# =========================
suma = 0
numero = int(input("\n[4] Ingrese un número "))
while numero != 0:
    suma += numero
    numero = int(input("Ingrese otro número (0 para terminar): "))      
print(f"La suma total es: {suma}")

# =========================
# 5) Adivina el número entre 1 y 10
# =========================
numero = random.randint(1, 10)
intentos = 0
adivina = int(input("\n[5] Adivina el número entre 1 y 10: "))
while adivina != numero:
    adivina = int(input("Incorrecto. Intenta de nuevo: "))
    intentos += 1
print(f"¡Correcto! El número era {numero}. Lo adivinaste en {intentos} intentos.")

# =========================
# 6) Numeros pares del 100 al 0
# =========================
for i in range(100,-1,-2):
    print(i)

# =========================
# 7) Suma de enteros desde 0 hasta un número ingresado
# =========================
numero = int(input("\n[7] Ingrese un número entero positivo: "))
suma = 0
for i in range(0, numero + 1):  
    suma += i
print(f"La suma de los números desde 0 hasta {numero} es: {suma}")

# =========================
# 8) Clasificación de números ingresados (pares/impares y positivos/negativos)
# =========================

pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range(100):  # <-- Cantidad de números a ingresar
    numero = int(input(f"\n[8] Ingrese un número: "))
    if numero % 2 == 0:# <-- Clasificación par/impar
        pares += 1
    else:
        impares += 1 
    if numero > 0:# <-- Clasificación positivo/negativo
        positivos += 1
    elif numero < 0:
        negativos += 1
print(f"Números pares: {pares}, Números impares: {impares}, Números positivos: {positivos}, Números negativos: {negativos}")

# =========================
# 9) media de 100 números enteros ingresados 
# =========================
suma = 0
for i in range(100): # <-- Cantidad de números a ingresar
    intero = int(input(f"\n[9] Ingrese un número entero: "))
    suma += intero
    media = suma / (i + 1)
    print(f"Suma actual: {suma}, Media actual: {media:.2f}")

# =========================
# 10) Invertir un número
# =========================
invertido = 0  # acumulador para el número invertido
numero = int(input("\n[10] Ingrese un número: "))
negativo = numero < 0
numero = abs(numero)  # Trabajar con el valor absoluto para simplificar
while numero > 0: 
    invertido = invertido * 10 + (numero % 10)  # extrae el último dígito y lo agrega al invertido
    numero //= 10  # elimina el último dígito del número original
if negativo:
    invertido = -invertido  # Restaurar el signo negativo si es necesario
print(f"Número invertido: {invertido}") 
