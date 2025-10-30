# ==========================#

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
# ==========================#
# ==========================#
# 7) Aprobados de Parciales (sets)
# ==========================#

# ==========================#
# 9) Agenda con tuplas como claves
# ==========================#

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
