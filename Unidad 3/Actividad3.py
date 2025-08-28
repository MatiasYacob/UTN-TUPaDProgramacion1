#=====================
#Imports de librerías
from statistics import mode, mean, median
import random
# ====================






# =========================
# 1) Mayor de edad
# =========================
edad = input("\n[1] Ingrese su edad: ")
if int(edad) >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")
# =========================
# 2) Notas de un estudiante
# =========================
nota = float(input("\n[2] Ingrese la nota del estudiante (0-10): "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")
# =========================
# 3) Ingresar Numero par
# =========================
numero = int(input("\n[3] Por favor, ingrese un número par "))
if numero % 2 == 0:
    print(f"Ha ingresado un número par")
else:
    print(f"Por favor, ingrese un número par.")
# ===================================
# 4) Ingresar Edad para ver Categoria
# ===================================
edad = int(input("\n[4] Ingrese su edad: "))
if edad <= 12:
    print("Categoría: Niño")
elif 13 <= edad <= 17:
    print("Categoría: Adolescente")
elif 18 <= edad < 30: # tengo 32 años me duele escribir esto
    print("Categoría: Adulto joven") 
else:
    print("Categoría: Adulto")
# ================================================
# 5) ingrese contraseña de entre 8 y 14 caracteres
# ================================================
password = input("\n[5] Ingrese una contraseña (8-14 caracteres): ")
if 8 <= len(password) <= 14:
    print("Ha ingresado una contraseña correcta.")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.")
# ==============================================
# 6) mode, mean y median de una lista de números
# ==============================================
numeros_aleatorios = [random.randint(1, 100) for _ in range(50)]
print("\n[6] Lista de números aleatorios:", numeros_aleatorios)
moda = mode(numeros_aleatorios)
print(f"Moda: {moda}")
media = mean(numeros_aleatorios)
print(f"Media: {media:.2f}")
mediana = median(numeros_aleatorios)
print(f"Mediana: {mediana}")
 #Tipo de sesgo
if media > mediana:
    print("Sesgo: Sesgo positivo (asimetría a la derecha)")
elif media < mediana:
    print("Sesgo: Sesgo negativo (asimetría a la izquierda)")
else:
    print("Sesgo: Simétrico (no hay sesgo)")
# ==============================================
# 7) Frase o palabra terminada en vocal? + !
# ==============================================
frase = input("\n[7] Ingrese una frase o palabra: ")
if frase[-1].lower() in 'aeiou':
    print(frase + "!")
else:
    print(frase)
# ========================================================
# 8) transformar el nombre según la opción elegida (1,2,3)
# ========================================================
nombre = input("\n[8] Ingrese su nombre: ")
opcion = input("Elija una opción (1: mayúsculas, 2: minúsculas, 3: capitalizar): ")
if opcion == '1':
    print(nombre.upper())
elif opcion == '2':
    print(nombre.lower())
elif opcion == '3':
    print(nombre.title())
else:
    print("Opción no válida.")
# ========================================================
# 9) categoria terremoto segun su magnitud (richter)
# ========================================================
magnitud = float(input("\n[9] Ingrese la magnitud del terremoto en la escala de Richter: "))
if magnitud < 3.0:
    print("Categoría: Muy leve (imperceptible)")
elif 3.0 <= magnitud < 4.0:
    print("Categoría: Leve (ligeramente perceptible)")
elif 4.0 <= magnitud < 5.0:
    print("Categoría: Moderado (sentido por personas, pero generalmente no causa daños)")
elif 5.0 <= magnitud < 6.0:
    print("Categoría: Fuerte (puede causar daños a estructuras débiles)")
elif 6.0 <= magnitud < 7.0:
    print("Categoría: Muy Fuerte (puede causar daños significativos)")
elif 7.0 <= magnitud:
    print("Categoría: Extremo (puede causar graves daños a gran escala)")
# ========================================================
# 10) Estación del año según hemisferio, mes y día.
# ========================================================
emisferio = input("\n[10] Ingrese el hemisferio (N/S): ").strip().lower()
mes = int(input("Ingrese el mes (numero del 1 al 12): "))
dia = int(input("Ingrese el día (numero del 1 al 31): "))

if emisferio not in ['n', 's']:
    print("Hemisferio no válido. Use 'N' para Norte o 'S' para Sur.")
else:
    if emisferio == 'n':  # Hemisferio Norte
        if (mes == 12 and dia >= 21) or (1 <= mes <= 2) or (mes == 3 and dia <= 20):
            estacion = "Invierno"
        elif (mes == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia <= 20):
            estacion = "Primavera"
        elif (mes == 6 and dia >= 21) or (7 <= mes <= 8) or (mes == 9 and dia <= 20):
            estacion = "Verano"
        else:
            estacion = "Otoño"
    else:  # Hemisferio Sur
        if (mes == 12 and dia >= 21) or (1 <= mes <= 2) or (mes == 3 and dia <= 20):
            estacion = "Verano"
        elif (mes == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia <= 20):
            estacion = "Otoño"
        elif (mes == 6 and dia >= 21) or (7 <= mes <= 8) or (mes == 9 and dia <= 20):
            estacion = "Invierno"
        else:
            estacion = "Primavera"

    print(f"Estación: {estacion}")
