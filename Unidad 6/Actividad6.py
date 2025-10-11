# ==========================#
# Helpers de validación
# me canse de errar inputs y tener que reiniciar el programa!!!
# ==========================#
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

# ==========================#
# 1) imprimir_hola_mundo
# ==========================#
def imprimir_hola_mundo():
    print("[1] Hola Mundo!")

imprimir_hola_mundo()

# ==========================#
# 2) saludar_usuario(nombre)
# ==========================#
def saludar_usuario(nombre):
    return f"[2] Hola {nombre}!"

nombre = input_str("\n[2] Ingrese su nombre: ")
print(saludar_usuario(nombre))

# ==========================#
# 3) informacion_personal(nombre, apellido, edad, residencia)
# ==========================#
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"[3] Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

nombre = input_str("\n[3] Nombre: ")
apellido = input_str("[3] Apellido: ")
edad = input_int("[3] Edad: ", min_value=0)
residencia = input_str("[3] Lugar de residencia: ", allow_empty=False)
informacion_personal(nombre, apellido, edad, residencia)

# ==========================#
# 4) calcular_area_circulo y calcular_perimetro_circulo
# ==========================#
import math

def calcular_area_circulo(radio):
    return math.pi * radio**2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

radio = input_float("\n[4] Ingrese el radio del círculo: ", min_value=0)
print("[4] Área:", round(calcular_area_circulo(radio), 2))
print("[4] Perímetro:", round(calcular_perimetro_circulo(radio), 2))

# ==========================#
# 5) segundos_a_horas(segundos)
# ==========================#
def segundos_a_horas(segundos):
    return segundos / 3600

segundos = input_int("\n[5] Ingrese la cantidad de segundos: ", min_value=0)
print("[5] Equivalente en horas:", round(segundos_a_horas(segundos), 2))

# ==========================#
# 6) tabla_multiplicar(numero)
# ==========================#
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"[6] {numero} x {i} = {numero * i}")

numero = input_int("\n[6] Ingrese un número para mostrar su tabla de multiplicar: ")
tabla_multiplicar(numero)

# ==========================#
# 7) operaciones_basicas(a, b)
# ==========================#
def operaciones_basicas(a, b):
    return (a + b, a - b, a * b, a / b)

a = input_float("\n[7] Primer número: ")
b = input_float("[7] Segundo número (≠0 para dividir): ")
while b == 0:
    print("[7] No se puede dividir por cero.")
    b = input_float("[7] Segundo número (≠0 para dividir): ")

suma, resta, mult, div = operaciones_basicas(a, b)
print(f"[7] Suma: {suma}, Resta: {resta}, Multiplicación: {mult}, División: {round(div, 2)}")

# ==========================#
# 8) calcular_imc(peso, altura_cm)
# ==========================#
def calcular_imc_desde_cm(peso_kg, altura_cm):
    altura_m = altura_cm / 100.0
    return peso_kg / (altura_m ** 2)

peso = input_float("\n[8] Peso (kg): ", min_value=0.0)
altura_cm = input_float("[8] Altura (cm): ", min_value=30.0, max_value=300.0)
print("[8] Su IMC es:", round(calcular_imc_desde_cm(peso, altura_cm), 2))

# ==========================#
# 9) celsius_a_fahrenheit(celsius)
# ==========================#
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

temp_c = input_float("\n[9] Temperatura en °C: ")
print("[9] Equivalente en °F:", round(celsius_a_fahrenheit(temp_c), 2))

# ==========================#
# 10) calcular_promedio(a, b, c)
# ==========================#
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

a = input_float("\n[10] Primer número: ")
b = input_float("[10] Segundo número: ")
c = input_float("[10] Tercer número: ")
print("[10] Promedio:", round(calcular_promedio(a, b, c), 2))

# ==========================#
# Fin del TP - Funciones
# ==========================#
print("\n[Fin] Trabajo Práctico de Funciones finalizado correctamente.")
