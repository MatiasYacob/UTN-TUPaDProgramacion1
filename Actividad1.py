# =========================
# 1) Hola Mundo 
# =========================
print("Hola Mundo!")

# =========================
# 2) Saludo con nombre
# =========================
nombre = input("\n[2] Ingrese su nombre: ")
print(f"Hola {nombre}!")

# =========================
# 3) Nombre, apellido, edad, residencia
# =========================
nombre2 = input("\n[3] Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")
print(f"Soy {nombre2} {apellido}, tengo {edad} años y vivo en {residencia}.")

# =========================
# 4) Área y perímetro de un círculo (pi = 3.14)
# =========================
radio = float(input("\n[4] Ingrese el radio del círculo: "))
area = 3.14 * (radio ** 2)
perimetro = 2 * 3.14 * radio
print(f"El área del círculo es: {area:.2f}")
print(f"El perímetro del círculo es: {perimetro:.2f}")

# =========================
# 5) Segundos a horas
# =========================
segundos = int(input("\n[5] Ingrese la cantidad de segundos: "))
horas = segundos / 3600
print(f"{segundos} segundos equivalen a {horas:.2f} horas")

# =========================
# 6) Tabla de multiplicar (1 al 10)
# =========================
numero = int(input("\n[6] Ingrese un número para su tabla de multiplicar: "))
print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

# =========================
# 7) Operaciones con dos enteros (distintos de 0)
# =========================
num1 = int(input("\n[7] Ingrese el primer número (distinto de 0): "))
num2 = int(input("Ingrese el segundo número (distinto de 0): "))
if num1 != 0 and num2 != 0:
    print(f"Suma: {num1} + {num2} = {num1 + num2}")
    print(f"Resta: {num1} - {num2} = {num1 - num2}")
    print(f"Multiplicación: {num1} x {num2} = {num1 * num2}")
    print(f"División: {num1} / {num2} = {(num1 / num2):.2f}")
else:
    print("Error: Los números deben ser distintos de 0.")


# =========================
# 8) Índice de Masa Corporal (IMC)
# =========================
peso = float(input("\n[8] Ingrese su peso en kilogramos: "))
altura_cm = float(input("Ingrese su altura en centímetros: "))

# Convertir centímetros a metros
altura = altura_cm / 100  

# Calcular IMC
imc = peso / (altura ** 2)

# Mostrar resultado
print(f"Su índice de masa corporal (IMC) es: {imc:.2f}")


# =========================
# 9) Celsius a Fahrenheit
# =========================
celsius = float(input("\n[9] Ingrese la temperatura en °C: "))
fahrenheit = (9/5) * celsius + 32
print(f"{celsius}°C equivalen a {fahrenheit:.2f}°F")

# =========================
# 10) Promedio de tres números
# =========================
n1 = float(input("\n[10] Ingrese el primer número: "))
n2 = float(input("Ingrese el segundo número: "))
n3 = float(input("Ingrese el tercer número: "))
promedio = (n1 + n2 + n3) / 3
print(f"El promedio de {n1}, {n2} y {n3} es: {promedio:.2f}")
