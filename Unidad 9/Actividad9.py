import time

#==========================#
# [1] Factorial recursivo
#==========================#

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def opcion_factoriales():
    n = int(input("[1] Ingrese un número (entero no negativo): "))

    if n < 0:
        print("[1] Error: el número debe ser entero no negativo.\n")
        return

    print("\n[1] Calculando factoriales...")
    time.sleep(1)
    print()  # Línea en blanco

    # Factorial puntual
    print(f"[1] Factorial de {n}: {factorial(n)}\n")

    # Factoriales desde 1 hasta n
    print(f"[1] Factoriales desde 1 hasta {n}:\n")
    for i in range(1, n + 1):
        time.sleep(0.2)
        print(f"[1] • {i}! = {factorial(i)}")

    print()


#==========================#
# [2] Fibonacci recursivo
#==========================#

def fibonacci(pos):
    if pos == 0:
        return 0
    if pos == 1:
        return 1
    return fibonacci(pos - 1) + fibonacci(pos - 2)

def opcion_fibonacci():

    n = int(input("[2] Ingrese una posición (entero no negativo): "))

    # Validación de no negativo
    if n < 0:
        print("\n[2] Error: la posición debe ser un entero no negativo.\n")
        return

    # Limitante para evitar cuelgues
    if n > 30:
        print("\n[2] El número es demasiado grande para calcularlo recursivamente.")
        print("[2] Por favor ingrese un valor menor o igual a 30.\n")
        return

    print("\n[2] Generando serie Fibonacci...")
    time.sleep(1)

    # Mostrar valor puntual
    print(f"[2] El valor de Fibonacci en la posición {n} es: {fibonacci(n)}\n")

    # Mostrar serie completa
    print("[2] Serie:\n")
    for i in range(n + 1):
        time.sleep(0.2)
        print(f"{fibonacci(i)}", end=" ")

    print("\n")


#==========================#
# [3] Potencia n^m
#==========================#

def potencia(base, exp):
    if exp == 0:
        return 1
    return base * potencia(base, exp - 1)

def opcion_potencia():

    base = int(input("[3] Ingrese la base: "))
    exp = int(input("[3] Ingrese el exponente (entero >= 0): "))

    if exp < 0:
        print("\n[3] Error: el exponente debe ser un entero mayor o igual a 0.\n")
        return

    print("\n[3] Calculando potencia...")
    time.sleep(1)

    res = potencia(base, exp)

    print(f"[3] {base}^{exp} = {res}\n")


#==========================#
# [4] Decimal a binario
#==========================#

def decimal_a_binario(n):
    if n < 2:
        return str(n)
    return decimal_a_binario(n // 2) + str(n % 2)

def opcion_decimal_a_binario():

    num = int(input("[4] Ingrese un número decimal (entero >= 0): "))

    if num < 0:
        print("\n[4] Error: solo se admiten enteros no negativos.\n")
        return

    print("\n[4] Convirtiendo número...")
    time.sleep(1)
    print(f"[4] Binario: {decimal_a_binario(num)}\n")


#==========================#
# [5] Es palíndromo
#==========================#

def es_palindromo(txt):
    if len(txt) <= 1:
        return True
    if txt[0] != txt[-1]:
        return False
    return es_palindromo(txt[1:-1])

def opcion_palindromo():

    palabra = input("[5] Ingrese una palabra: ").lower()
    print("\n[5] Verificando palíndromo...")
    time.sleep(1)
    if es_palindromo(palabra):
        print(f"[5] '{palabra}' ES un palíndromo.\n")
    else:
        print(f"[5] '{palabra}' NO es un palíndromo.\n")


#==========================#
# [6] Suma de dígitos
#==========================#

def suma_digitos(n):
    n = abs(n)
    if n < 10:
        return n
    return (n % 10) + suma_digitos(n // 10)

def opcion_suma_digitos():

    num = int(input("[6] Ingrese un número: "))
    print("\n[6] Sumando dígitos...")
    time.sleep(1)
    print(f"[6] Resultado: {suma_digitos(num)}\n")


#==========================#
# [7] Cantidad de bloques en pirámide
#==========================#

def contar_bloques(n):
    if n <= 1:
        return max(0, n)
    return n + contar_bloques(n - 1)

def opcion_bloques():

    niveles = int(input("[7] Ingrese la cantidad del nivel inferior (entero > 0): "))

    if niveles <= 0:
        print("\n[7] Error: la cantidad de bloques debe ser mayor que 0.\n")
        return

    print("\n[7] Calculando bloques totales...\n")

    # Parte visual del cálculo
    acumulado = 0
    for i in range(niveles, 0, -1):
        acumulado += i
        print(f"[7] Sumando nivel {i}: total parcial = {acumulado}")

    # Mostrar total
    total = contar_bloques(niveles)
    print(f"\n[7] Total de bloques necesarios: {total}\n")

    # Dibujar la pirámide con asteriscos
    print("[7] Representación visual de la pirámide:\n")
    for i in range(niveles, 0, -1):
        print("[7] " + "*" * i)

    print()


#==========================#
# [8] Contar ocurrencias de un dígito
#==========================#

def contar_digito(num, dig):
    num = abs(num)
    if num == 0:
        return 0
    ultimo = num % 10
    return (1 if ultimo == dig else 0) + contar_digito(num // 10, dig)

def opcion_contar_digito():

    num = int(input("[8] Ingrese un número positivo: "))

    # Validación: número debe ser positivo o cero
    if num < 0:
        print("[8] Error: el número debe ser positivo.\n")
        return

    dig = int(input("[8] Dígito a buscar (0-9): "))

    # Validación del dígito
    if dig < 0 or dig > 9:
        print("[8] Error: el dígito debe estar entre 0 y 9.\n")
        return

    # Caso especial: 0
    if num == 0 and dig == 0:
        print("\n[8] Contando dígitos...")
        print("[8] El dígito 0 aparece 1 vez en 0.\n")
        return

    print("\n[8] Contando dígitos...")

    cantidad = contar_digito(num, dig)
    print(f"[8] El dígito {dig} aparece {cantidad} veces en {num}.\n")


#==========================#
# Menú principal
#==========================#

def mostrar_menu():
    print("========== TP7 - RECURSIVIDAD ==========")
    print("1) Factorial")
    print("2) Fibonacci")
    print("3) Potencia")
    print("4) Decimal a binario")
    print("5) Palíndromo")
    print("6) Suma de dígitos")
    print("7) Bloques totales")
    print("8) Contar dígito")
    print("0) Salir")
    print("========================================")


def main():
    while True:
        mostrar_menu()
        opc = input("Seleccione una opción: ")

        if opc == "1":
            opcion_factoriales()
        elif opc == "2":
            opcion_fibonacci()
        elif opc == "3":
            opcion_potencia()
        elif opc == "4":
            opcion_decimal_a_binario()
        elif opc == "5":
            opcion_palindromo()
        elif opc == "6":
            opcion_suma_digitos()
        elif opc == "7":
            opcion_bloques()
        elif opc == "8":
            opcion_contar_digito()
        elif opc == "0":
            print("[0] Saliendo del programa...")
            time.sleep(1)
            break
        else:
            print("[X] Opción inválida.\n")


if __name__ == "__main__":
    main()
