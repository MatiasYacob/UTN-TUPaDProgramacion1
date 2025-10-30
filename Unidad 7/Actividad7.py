# ==========================
# Helpers de validación 
# ==========================

def input_str(prompt, allow_empty=False, default=None):
    """
    Lee una cadena. Recorta espacios.
    - allow_empty: si True, permite vacío ("").
    - default: si no es None y el usuario presiona Enter, devuelve default.
    """
    while True:
        s = input(prompt)
        if s is None:
            s = ""
        s = s.strip()

        if s == "" and default is not None:
            return default

        if s or allow_empty:
            return s

        print("[!] Entrada vacía. Intente nuevamente.")


def input_float(prompt, min_value=None, max_value=None, default=None):
    """
    Lee un float. Acepta coma o punto para decimales.
    - min_value / max_value: límites (incluyentes).
    - default: si no es None y el usuario presiona Enter, devuelve default (validado contra límites si los hay).
    """
    while True:
        s = input(prompt).strip()

        if s == "" and default is not None:
            v = float(str(default).replace(",", "."))
            if (min_value is not None and v < min_value):
                print(f"[!] El valor por defecto no puede ser menor que {min_value}.")
                continue
            if (max_value is not None and v > max_value):
                print(f"[!] El valor por defecto no puede ser mayor que {max_value}.")
                continue
            return v

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


def input_int(prompt, min_value=None, max_value=None, default=None):
    """
    Lee un entero.
    - min_value / max_value: límites (incluyentes).
    - default: si no es None y el usuario presiona Enter, devuelve default (validado).
    """
    while True:
        s = input(prompt).strip()

        if s == "" and default is not None:
            try:
                v = int(default)
            except ValueError:
                print("[!] El valor por defecto no es un entero válido.")
                continue
            if min_value is not None and v < min_value:
                print(f"[!] El valor por defecto no puede ser menor que {min_value}.")
                continue
            if max_value is not None and v > max_value:
                print(f"[!] El valor por defecto no puede ser mayor que {max_value}.")
                continue
            return v

        try:
            v = int(s)
        except ValueError:
            print("[!] Debe ingresar un número entero válido.")
            continue

        if min_value is not None and v < min_value:
            print(f"[!] El valor no puede ser menor que {min_value}.")
            continue
        if max_value is not None and v > max_value:
            print(f"[!] El valor no puede ser mayor que {max_value}.")
            continue
        return v


def input_opcion(prompt, opciones_validas, default=None):
    """
    Devuelve la opción elegida en minúscula si es válida.
    - opciones_validas: iterable con opciones (e.g. {'a','b','salir'}).
    - default: opción por defecto si el usuario presiona Enter (también validada).
    """
    opciones_lower = {str(o).lower() for o in opciones_validas}
    opciones_list = sorted(opciones_lower)

    while True:
        s = input(prompt).strip().lower()

        if s == "" and default is not None:
            d = str(default).lower()
            if d in opciones_lower:
                return d
            print(f"[!] Opción por defecto inválida. Debe ser una de: {opciones_list}")
            continue

        if s in opciones_lower:
            return s

        print(f"[!] Opción inválida. Opciones válidas: {opciones_list}")


# ==========================#
# 1) Precios de Frutas
# ==========================#

precios_frutas = {
    'Banana': 1200,
    'Ananá': 2500,
    'Melón': 3000,
    'Uva': 1450
}

# Agregar nuevas frutas
precios_frutas.update({
    'Naranja': 1200,
    'Manzana': 1500,
    'Pera': 2300
})

# Mostrar el diccionario ordenado
print("\n[1] Listado de frutas y precios actualizados:\n")
for fruta in sorted(precios_frutas):
    print(f"[1] {fruta}: ${precios_frutas[fruta]}")


# ==========================#
# 2) Actualización de precios
# ==========================#

# Cambiar los precios directamente (cambio plano)
precios_frutas['Banana'] = 1500
precios_frutas['Manzana'] = 1600
precios_frutas['Melón'] = 2800

print("\n[2] Precios actualizados:\n")
for fruta in sorted(precios_frutas):
    print(f"[2] {fruta}: ${precios_frutas[fruta]}")


# ==========================#
# 3) Lista de nombres de frutas
# ==========================#

# Crear una lista que contenga únicamente las frutas (las claves del diccionario)
lista_frutas = list(precios_frutas.keys())

print("\n[3] Lista de nombres de frutas (sin precios):\n")
for fruta in sorted(lista_frutas):
    print(f"[3] {fruta}")


# ==========================#
# 4) Agenda Telefónica
# ==========================#

agenda = {}

print("\n[4] Carga de contactos en la agenda telefónica (máximo 5, o escriba 'salir' para finalizar):")

while len(agenda) < 5:
    nombre = input_str("[4] Ingrese el nombre del contacto: ")
    if nombre.lower() == "salir":
        break

    telefono = input_int("[4] Ingrese el número de teléfono: ", min_value=0)

    if nombre in agenda:
        print("[4] Ese contacto ya existe; se actualiza el número.")
    agenda[nombre] = telefono

print("\n[4] Agenda cargada:\n")
for nombre, telefono in sorted(agenda.items()):
    print(f"[4] {nombre}: {telefono}")

# Bucle de consultas múltiples
print("\n[4] Consultas de agenda (escriba 'salir' para finalizar):")
while True:
    consulta = input_str("[4] Ingrese el nombre del contacto a buscar: ")
    if consulta.lower() == "salir":
        break

    if consulta in agenda:
        print(f"[4] El número de {consulta} es: {agenda[consulta]}")
    else:
        print(f"[4] El contacto '{consulta}' no se encuentra en la agenda.")


# ==========================#
# 5) Palabras únicas y conteo de frecuencia
# ==========================#

print("\n[5] Análisis de palabras únicas y su frecuencia en una frase.\n")

frase = input_str("[5] Ingrese una frase: ")

# Normalizamos la frase: minúsculas y sin puntuación básica
for c in ",.;:!?¡¿\"'()[]{}-_":
    frase = frase.replace(c, "")

palabras = frase.lower().split()

# Set de palabras únicas
palabras_unicas = set(palabras)

print("\n[5] Palabras únicas encontradas (ordenadas):")
for palabra in sorted(palabras_unicas):
    print(f"[5] {palabra}")

# Diccionario de frecuencias
recuento = {}
for palabra in palabras:
    recuento[palabra] = recuento.get(palabra, 0) + 1

print("\n[5] Frecuencia de cada palabra (ordenadas por palabra):")
for palabra in sorted(recuento.keys()):
    print(f"[5] '{palabra}': {recuento[palabra]} vez/veces")


# ==========================#
# 6) Promedio de Notas de Estudiantes
# ==========================#

alumnos = {}

print("\n[6] Ingreso de nombres y notas de los alumnos (máximo 3).")

while len(alumnos) < 3:
    nombre = input_str("[6] Ingrese el nombre del alumno (o 'salir' para finalizar): ")
    if nombre.lower() == "salir":
        break

    notas = []
    for n in range(1, 4):
        nota = input_float(f"[6] Ingrese la nota {n} de {nombre}: ", min_value=0, max_value=10)
        notas.append(nota)

    alumnos[nombre] = tuple(notas)  # Tupla de 3 notas

print("\n[6] Promedios de los alumnos:")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"[6] {nombre}: promedio {promedio:.2f}")


# ==========================#
# 7) Aprobados de Parciales (sets)
# ==========================#

print("\n[7] Ingreso de alumnos que aprobaron el Parcial 1 (escriba 'salir' para finalizar):")
parcial1 = set()
while True:
    nombre = input_str("[7] Nombre del alumno (P1): ")
    if nombre.lower() == "salir":
        break
    if nombre:
        parcial1.add(nombre)

print("\n[7] Ingreso de alumnos que aprobaron el Parcial 2 (escriba 'salir' para finalizar):")
parcial2 = set()
while True:
    nombre = input_str("[7] Nombre del alumno (P2): ")
    if nombre.lower() == "salir":
        break
    if nombre:
        parcial2.add(nombre)

# Cálculos con conjuntos
ambos = parcial1 & parcial2          # Intersección
solo_uno = parcial1 ^ parcial2       # Diferencia simétrica
al_menos_uno = parcial1 | parcial2   # Unión

# Mostrar resultados (ordenados)
print("\n[7] Alumnos que aprobaron AMBOS parciales:")
for alumno in sorted(ambos):
    print(f"[7] {alumno}")

print("\n[7] Alumnos que aprobaron SOLO UNO de los parciales:")
for alumno in sorted(solo_uno):
    print(f"[7] {alumno}")

print("\n[7] Alumnos que aprobaron AL MENOS UNO de los parciales:")
for alumno in sorted(al_menos_uno):
    print(f"[7] {alumno}")


# ==========================#
# 8) Diccionario de Stock
# ==========================#

# Diccionario predefinido
stock = {
    "Aceite 1L": 25,
    "Filtro De Aire": 15,
    "Bujía Ngk": 40,
    "Anticongelante 1L": 30,
    "Lubricante 5W30": 20
}

print("\n[8] Gestión de stock de productos.")
print("[8] Opciones: consultar, agregar, listar o salir.")

while True:
    opcion = input_opcion("[8] Ingrese una opción: ", {"consultar", "agregar", "listar", "salir"})

    if opcion == "consultar":
        producto = input_str("[8] Ingrese el nombre del producto a consultar: ")
        producto_norm = producto.strip().title()
        if producto_norm in stock:
            print(f"[8] Stock actual de {producto_norm}: {stock[producto_norm]} unidades.")
        else:
            print(f"[8] El producto '{producto}' no existe en el inventario.")

    elif opcion == "agregar":
        producto = input_str("[8] Ingrese el nombre del producto: ")
        producto_norm = producto.strip().title()
        cantidad = input_int("[8] Ingrese la cantidad a agregar: ", min_value=0)

        if producto_norm in stock:
            stock[producto_norm] += cantidad
            print(f"[8] Stock actualizado: {producto_norm} ahora tiene {stock[producto_norm]} unidades.")
        else:
            stock[producto_norm] = cantidad
            print(f"[8] Producto '{producto_norm}' agregado con {cantidad} unidades.")

    elif opcion == "listar":
        if not stock:
            print("[8] No hay productos cargados.")
        else:
            print("\n[8] Inventario actual:")
            for nombre, cant in sorted(stock.items()):
                print(f"[8] {nombre}: {cant} unidades")

    elif opcion == "salir":
        print("[8] Saliendo del módulo de stock.")
        break


# ==========================#
# 9) Agenda con tuplas como claves
# ==========================#

agenda = {}

print("\n[9] Gestión de agenda (día y hora).")
print("[9] Opciones: agregar, consultar, ver, o salir.")

while True:
    opcion = input_opcion("[9] Ingrese una opción: ", {"agregar", "consultar", "ver", "salir"})

    if opcion == "agregar":
        dia = input_str("[9] Ingrese el día del evento: ")
        if dia.lower() == "salir":
            continue

        hora = input_str("[9] Ingrese la hora del evento (ej. 14:00): ")
        evento = input_str("[9] Describa el evento: ")

        clave = (dia, hora)
        agenda[clave] = evento
        print(f"[9] Evento agregado para {dia} a las {hora}.")

    elif opcion == "consultar":
        dia = input_str("[9] Ingrese el día a consultar: ")
        if dia.lower() == "salir":
            continue

        hora = input_str("[9] Ingrese la hora a consultar: ")
        clave = (dia, hora)

        if clave in agenda:
            print(f"[9] Evento para {dia} a las {hora}: {agenda[clave]}")
        else:
            print(f"[9] No hay eventos registrados para {dia} a las {hora}.")

    elif opcion == "ver":
        if not agenda:
            print("[9] No hay eventos cargados en la agenda.")
        else:
            print("\n[9] Agenda completa:")
            for (dia, hora), evento in sorted(agenda.items()):
                print(f"[9] {dia} {hora}: {evento}")

    elif opcion == "salir":
        print("[9] Saliendo de la agenda.")
        break


# ==========================#
# 10) Diccionario invertido (capital → país)
# ==========================#

# Diccionario base: país → capital
paises = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Chile": "Santiago",
    "Uruguay": "Montevideo",
    "Paraguay": "Asunción"
}

print("\n[10] Diccionario original (país → capital):")
for pais, capital in paises.items():
    print(f"[10] {pais} → {capital}")

# Crear el diccionario invertido (capital → país)
invertido = {capital: pais for pais, capital in paises.items()}

print("\n[10] Diccionario invertido (capital → país):")
for capital, pais in invertido.items():
    print(f"[10] {capital} → {pais}")
