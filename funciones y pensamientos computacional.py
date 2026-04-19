def calcular_billetes(monto):
    # Validar que sea múltiplo de 20
    if monto % 20 != 0:
        print("Error: el monto debe ser múltiplo de 20")
        return None

    # Calcular billetes
    b200 = monto // 200
    monto = monto % 200

    b100 = monto // 100
    monto = monto % 100

    b50 = monto // 50
    monto = monto % 50

    b20 = monto // 20

    # Mostrar resultado
    print(f"{b200}x Q200, {b100}x Q100, {b50}x Q50, {b20}x Q20")

    # Retornar valores (opcional)
    return (b200, b100, b50, b20)


# =========================
# PRUEBA DEL PROGRAMA
# =========================

monto = int(input("Ingrese el monto en quetzales: "))
calcular_billetes(monto)











# validador de contraseña
def tiene_mayuscula(texto):
    for c in texto:
        if c.isupper():
            return True
    return False

def tiene_digito(texto):
    for c in texto:
        if c.isdigit():
            return True
    return False

def tiene_especial(texto):
    especiales = "!@#$%"
    for c in texto:
        if c in especiales:
            return True
    return False

def validar_password(password):
    if len(password) < 8:
        return False
    if not tiene_mayuscula(password):
        return False
    if not tiene_digito(password):
        return False
    if not tiene_especial(password):
        return False
    return True

def diagnosticar_password(password):
    errores = []

    if len(password) < 8:
        errores.append("Debe tener al menos 8 caracteres")
    if not tiene_mayuscula(password):
        errores.append("Debe tener al menos una letra mayúscula")
    if not tiene_digito(password):
        errores.append("Debe tener al menos un dígito")
    if not tiene_especial(password):
        errores.append("Debe tener al menos un carácter especial (!, @, #, $, %)")

    if len(errores) == 0:
        print("La contraseña es válida")
    else:
        print("La contraseña NO es válida. Errores:")
        for e in errores:
            print("-", e)









# converosr universal de temperatura
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










# analicis de calificaciones
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









# generador tabla de multiplicar
def tabla(n):
    print(f"--- Tabla del {n} ---")
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")
    print()  # espacio


# Verifica si un número es primo
def es_primo(n):
    if n < 2:
        return False
    
    # solo hasta la raíz cuadrada
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    
    return True


# Imprime tablas solo de números primos
def tablas_primos(limite):
    for num in range(2, limite + 1):
        if es_primo(num):
            tabla(num)


# PRUEBA
tablas_primos(10)









# Cifra un solo carácter

def cifrar_caracter(c, desplazamiento):
    if c.isalpha():  # solo letras
        if c.islower():
            base = ord('a')
        else:
            base = ord('A')
        
        # posición en el alfabeto (0-25)
        posicion = ord(c) - base
        
        # aplicar desplazamiento con efecto circular
        nueva_pos = (posicion + desplazamiento) % 26
        
        return chr(base + nueva_pos)
    else:
        return c  # no cambia si no es letra


# Cifra un mensaje completo
def cifrar_mensaje(mensaje, desplazamiento):
    resultado = ""
    for c in mensaje:
        resultado += cifrar_caracter(c, desplazamiento)
    return resultado


# Descifra un mensaje (desplazamiento inverso)
def descifrar_mensaje(mensaje, desplazamiento):
    return cifrar_mensaje(mensaje, -desplazamiento)


# PRUEBAS
print(cifrar_mensaje("hola", 3))          # krod
print(cifrar_mensaje("Hola Mundo!", 5))  # Mtqf Rzsit!
print(descifrar_mensaje("krod", 3))      # hola







# calculadora de propinas
def calcular_propina(subtotal, porcentaje):
    return subtotal * (porcentaje / 100)


def calcular_total(subtotal, propina):
    return subtotal + propina


def dividir_cuenta(total, personas):
    if personas <= 0:
        return "Error: número de personas inválido"
    return total / personas


def aplicar_descuento(subtotal, descuento_pct):
    return subtotal - (subtotal * (descuento_pct / 100))


# Menú
def mostrar_menu():
    print("\n--- CALCULADORA DE PROPINAS ---")
    print("1. Calcular propina")
    print("2. Dividir la cuenta")
    print("3. Aplicar descuento + propina")
    print("4. Salir")


# Función principal
def main():
    while True:
        mostrar_menu()
        
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            try:
                subtotal = float(input("Subtotal: Q"))
                print("Sugerencias: 10%, 15%, 20%")
                porcentaje = float(input("Porcentaje de propina: "))
                
                propina = calcular_propina(subtotal, porcentaje)
                total = calcular_total(subtotal, propina)
                
                print(f"Propina: Q{propina:.2f}")
                print(f"Total a pagar: Q{total:.2f}")
            except:
                print("Error: ingresa valores numéricos válidos")


        elif opcion == "2":
            try:
                total = float(input("Total de la cuenta: Q"))
                personas = int(input("Número de personas: "))
                
                resultado = dividir_cuenta(total, personas)
                
                if isinstance(resultado, str):
                    print(resultado)
                else:
                    print(f"Cada persona paga: Q{resultado:.2f}")
            except:
                print("Error: datos inválidos")


        elif opcion == "3":
            try:
                subtotal = float(input("Subtotal: Q"))
                descuento = float(input("Descuento (%): "))
                porcentaje = float(input("Propina (%): "))
                
                nuevo_subtotal = aplicar_descuento(subtotal, descuento)
                propina = calcular_propina(nuevo_subtotal, porcentaje)
                total = calcular_total(nuevo_subtotal, propina)
                
                print(f"Subtotal con descuento: Q{nuevo_subtotal:.2f}")
                print(f"Propina: Q{propina:.2f}")
                print(f"Total a pagar: Q{total:.2f}")
            except:
                print("Error: datos inválidos")


        elif opcion == "4":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida")


# Ejecutar
main()
