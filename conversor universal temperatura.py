def celsius_a_fahrenheit(c):
    return c * 9/5 + 32

def fahrenheit_a_celsius(f):
    return (f - 32) * 5/9

def celsius_a_kelvin(c):
    return c + 273.15


def convertir(valor, origen, destino):
    origen = origen.upper()
    destino = destino.upper()

    # Validar escalas
    if origen not in ['C', 'F', 'K'] or destino not in ['C', 'F', 'K']:
        return None

    # Si son iguales
    if origen == destino:
        return valor

    # PASO 1: convertir a Celsius
    if origen == 'C':
        c = valor
    elif origen == 'F':
        c = fahrenheit_a_celsius(valor)
    elif origen == 'K':
        c = valor - 273.15

    # PASO 2: convertir desde Celsius al destino
    if destino == 'C':
        return c
    elif destino == 'F':
        return celsius_a_fahrenheit(c)
    elif destino == 'K':
        return celsius_a_kelvin(c)


# PRUEBAS
print(convertir(25, 'C', 'F'))   # 77.0
print(convertir(77, 'F', 'C'))   # 25.0
print(convertir(0, 'C', 'K'))    # 273.15
print(convertir(300, 'K', 'F'))  # 80.33 aprox
print(convertir(10, 'X', 'C'))   # None