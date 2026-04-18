# Función promedio
def promedio(notas):
    suma = 0
    for n in notas:
        suma += n
    return suma / len(notas)


# Función mayor (sin usar max)
def mayor(notas):
    mayor_valor = notas[0]
    for n in notas:
        if n > mayor_valor:
            mayor_valor = n
    return mayor_valor


# Función menor (sin usar min)
def menor(notas):
    menor_valor = notas[0]
    for n in notas:
        if n < menor_valor:
            menor_valor = n
    return menor_valor


# Contar aprobados
def contar_aprobados(notas, minimo=61):
    contador = 0
    for n in notas:
        if n >= minimo:
            contador += 1
    return contador


# Reporte completo
def reporte(notas):
    print("----- REPORTE DE CALIFICACIONES -----")
    print("Notas:", notas)
    print("Promedio:", promedio(notas))
    print("Nota más alta:", mayor(notas))
    print("Nota más baja:", menor(notas))
    print("Aprobados:", contar_aprobados(notas))


# PRUEBA
notas = [85, 42, 73, 61, 55, 90, 38, 77, 95, 60]
reporte(notas)